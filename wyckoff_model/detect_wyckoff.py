import pandas as pd
import numpy as np
from scipy.signal import find_peaks

def detect_wyckoff_events(df: pd.DataFrame, 
                          price_distance: int = 7, 
                          volume_percentile: float = 0.90) -> dict:
    """
    ฟังก์ชันสำหรับตรวจจับ Wyckoff Cycle 4 ระยะ (Accumulation, Markup, Distribution, Markdown)
    โดยการเชื่อมโยงเหตุการณ์สำคัญ
    """

    prices = df['close'].values
    volume = df['volume'].values
    highs = df['high'].values
    lows = df['low'].values
    
    # 1. กำหนดเกณฑ์ Volume สูงและหา Peaks/Troughs
    volume_threshold = np.percentile(volume, volume_percentile * 100)
    peaks, _ = find_peaks(prices, distance=price_distance)
    troughs, _ = find_peaks(-prices, distance=price_distance)
    
    events = {
        "BC": [], "SC": [], "UTAD": [], "Spring": [],
        "ACCUMULATION_TR": [], # Wyckoff Accumulation Pattern (Phase A-D)
        "DISTRIBUTION_TR": [], # Wyckoff Distribution Pattern (Phase A-D)
        "WYCKOFF_CYCLE": [] 
    }

    # 🅰️ ตรวจจับ Climax (BC/SC)
    for idx in peaks:
        if volume[idx] >= volume_threshold:
            events['BC'].append(idx)
                
    for idx in troughs:
        if volume[idx] >= volume_threshold:
            events['SC'].append(idx)
    
    # --- 🔍 ตรวจจับ Accumulation Pattern (SC -> Spring) ---
    for sc_idx in events['SC']:
        search_start = sc_idx + price_distance 
        search_end = min(len(df), sc_idx + 100) 
        if search_start >= search_end: continue
        
        tr_support = lows[sc_idx]
        tr_resistance = np.max(highs[search_start:search_end]) 
        
        for spring_idx in range(search_start, search_end):
            if lows[spring_idx] < tr_support * 0.98: # Low ทะลุ Support
                if prices[spring_idx] >= tr_support * 0.99 and prices[spring_idx] <= tr_resistance: # Close กลับเข้ากรอบ
                    events['Spring'].append(spring_idx)
                    events['ACCUMULATION_TR'].append({
                        "type": "ACCUMULATION",
                        "start_idx": sc_idx,
                        "end_idx": spring_idx,
                        "support": tr_support,
                        "resistance": tr_resistance
                    })
                    break 
                    
    # --- 🔍 ตรวจจับ Distribution Pattern (BC -> UTAD) ---
    for bc_idx in events['BC']:
        search_start = bc_idx + price_distance 
        search_end = min(len(df), bc_idx + 100) 
        if search_start >= search_end: continue
        
        tr_resistance = highs[bc_idx]
        tr_support = np.min(lows[search_start:search_end])
        
        for utad_idx in range(search_start, search_end):
            if highs[utad_idx] > tr_resistance * 1.02: # High ทะลุ Resistance
                if prices[utad_idx] <= tr_resistance * 1.01 and prices[utad_idx] >= tr_support: # Close กลับเข้ากรอบ
                    events['UTAD'].append(utad_idx)
                    events['DISTRIBUTION_TR'].append({
                        "type": "DISTRIBUTION",
                        "start_idx": bc_idx,
                        "end_idx": utad_idx,
                        "support": tr_support,
                        "resistance": tr_resistance
                    })
                    break 
    
    # 🅱️ จัดเรียง Wyckoff Cycle 4 ระยะ (Phase Sequencing)
    all_patterns = sorted(events['ACCUMULATION_TR'] + events['DISTRIBUTION_TR'], key=lambda x: x['start_idx'])
    
    if not all_patterns:
        return events
    
    for i in range(len(all_patterns)):
        current_pattern = all_patterns[i]
        
        # 1. Accumulation / Distribution Phase
        events['WYCKOFF_CYCLE'].append({
            "phase": current_pattern['type'], 
            "start_idx": current_pattern['start_idx'],
            "end_idx": current_pattern['end_idx'],
        })
        
        # 2. Markup / Markdown Phase
        trend_start_idx = current_pattern['end_idx']
        
        if i + 1 < len(all_patterns):
            trend_end_idx = all_patterns[i+1]['start_idx']
        else:
            trend_end_idx = len(df) - 1

        if current_pattern['type'] == "ACCUMULATION":
            events['WYCKOFF_CYCLE'].append({
                "phase": "MARKUP", 
                "start_idx": trend_start_idx,
                "end_idx": trend_end_idx,
            })
        elif current_pattern['type'] == "DISTRIBUTION":
            events['WYCKOFF_CYCLE'].append({
                "phase": "MARKDOWN",
                "start_idx": trend_start_idx,
                "end_idx": trend_end_idx,
            })
            
    events['BC'] = sorted(list(set(events['BC'])))
    events['SC'] = sorted(list(set(events['SC'])))
    events['UTAD'] = sorted(list(set(events['UTAD'])))
    events['Spring'] = sorted(list(set(events['Spring'])))

    return events