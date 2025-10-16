import pandas as pd
import numpy as np
from scipy.signal import find_peaks

def detect_wyckoff_events(df: pd.DataFrame, 
                          price_distance: int = 7, 
                          volume_percentile: float = 0.95) -> dict:


    prices = df['close'].values
    volume = df['volume'].values
    highs = df['high'].values
    lows = df['low'].values
    
    # 1. กำหนดเกณฑ์ Volume สูง (Climax Threshold)
    volume_threshold = np.percentile(volume, volume_percentile * 100)
    
    # 2. หาจุดสูงสุด/ต่ำสุดของราคา
    peaks, _ = find_peaks(prices, distance=price_distance)
    troughs, _ = find_peaks(-prices, distance=price_distance)
    
    events = {
        "BC": [],  # Buying Climax (จุดจบขาขึ้น)
        "SC": [],  # Selling Climax (จุดจบขาลง)
        "UTAD": [],# Upthrust After Distribution (กับดักขาขึ้น)
        "Spring": [], # Spring (กับดักขาลง)
    }

    # ==========================================================
    # 🅰️ ตรวจจับ Climax (BC/SC) - ใช้ Volume สูงเป็นเกณฑ์หลัก
    # ==========================================================
    
    # BC (Buying Climax): จุดสูงสุดของราคาที่เกิดพร้อม Volume สูง
    for idx in peaks:
        if volume[idx] >= volume_threshold:
            # เช็คว่า Volume สูงสุดในบริเวณใกล้เคียงหรือไม่ (ยืนยันว่าเป็น Climax)
            window = max(10, price_distance)
            start = max(0, idx - window)
            end = min(len(volume), idx + 1)
            
            if volume[idx] == np.max(volume[start:end]):
                events['BC'].append(idx)
                
    # SC (Selling Climax): จุดต่ำสุดของราคาที่เกิดพร้อม Volume สูง
    for idx in troughs:
        if volume[idx] >= volume_threshold:
            # เช็คว่า Volume สูงสุดในบริเวณใกล้เคียงหรือไม่ (ยืนยันว่าเป็น Climax)
            window = max(10, price_distance)
            start = max(0, idx - window)
            end = min(len(volume), idx + 1)
            
            if volume[idx] == np.max(volume[start:end]):
                events['SC'].append(idx)
                
    # ==========================================================
    # 🅱️ ตรวจจับ Spring/UTAD - กำหนดโดยขอบเขต (Trading Range)
    # (จำเป็นต้องหา Trading Range ก่อน ซึ่งซับซ้อน จึงใช้เงื่อนไขแบบง่ายก่อน)
    # ==========================================================

    # Note: การตรวจจับ Spring/UTAD ที่ถูกต้อง ต้องหา Trading Range (TR) 
    # จาก SC/BC และ AR (Automatic Rally/Reaction) ก่อน 
    # โค้ดด้านล่างเป็นแนวคิดเริ่มต้นที่ง่ายขึ้น

    # 1. กำหนดช่วงที่เกิด Climax (ใช้ BC/SC ที่หาได้เป็นจุดอ้างอิง)
    
    if len(events['SC']) >= 1 and len(events['BC']) >= 1:
        
        # ใช้ช่วงระหว่าง SC และ BC ที่ใกล้กันที่สุดเป็น Trading Range (TR) เบื้องต้น
        
        # 💡 Spring (Bear Trap - หลุดแนวรับ TR แล้วเด้งกลับ)
        # เราสมมติว่าแนวรับคือ Low ของ SC/ST ก่อนหน้า
        # และใช้เงื่อนไข 'ราคาต่ำสุดใหม่ แต่กลับมาปิดในกรอบ'

        # เนื่องจากต้องวิเคราะห์ความสัมพันธ์กับเหตุการณ์ก่อนหน้า 
        # เราจะจำลองการหา Spring/UTAD ใน Trading Range 100 แท่ง
        
        TR_LENGTH = 100 
        
        for i in range(len(prices) - TR_LENGTH):
            tr_prices = prices[i:i + TR_LENGTH]
            tr_lows = lows[i:i + TR_LENGTH]
            tr_highs = highs[i:i + TR_LENGTH]
            
            # หาขอบเขต TR (ใช้จุดต่ำสุด/สูงสุดของช่วง 50 แท่งแรกเป็น Support/Resistance)
            support = np.min(tr_lows[:50])
            resistance = np.max(tr_highs[:50])
            
            # 🔍 ตรวจจับ Spring (Phase C ของ Accumulation)
            # เงื่อนไข: ราคาลงไปต่ำกว่า Support และเด้งกลับเข้า TR อย่างรวดเร็ว
            # เราจะดูที่ 20 แท่งสุดท้ายของช่วง TR_LENGTH
            for j in range(TR_LENGTH - 20, TR_LENGTH):
                
                # ถ้า Low ทะลุ Support ลงไป
                if tr_lows[j] < support:
                    
                    # และ Close Price เด้งกลับมาเหนือ Support หรือเข้าใกล้
                    if tr_prices[j] > support * 0.99 and tr_prices[j] < resistance:
                        # Spring ที่ index i + j 
                        events['Spring'].append(i + j)
                        break # พบแล้วไปต่อ

            # 🔍 ตรวจจับ UTAD (Phase C ของ Distribution)
            # เงื่อนไข: ราคาขึ้นไปสูงกว่า Resistance แล้วร่วงกลับเข้า TR อย่างรวดเร็ว
            for j in range(TR_LENGTH - 20, TR_LENGTH):
                
                # ถ้า High ทะลุ Resistance ขึ้นไป
                if tr_highs[j] > resistance:
                    
                    # และ Close Price ร่วงกลับมาใต้ Resistance หรือเข้าใกล้
                    if tr_prices[j] < resistance * 1.01 and tr_prices[j] > support:
                        # UTAD ที่ index i + j
                        events['UTAD'].append(i + j)
                        break # พบแล้วไปต่อ

    # ลบ Index ซ้ำ (ถ้ามี)
    events['BC'] = sorted(list(set(events['BC'])))
    events['SC'] = sorted(list(set(events['SC'])))
    events['UTAD'] = sorted(list(set(events['UTAD'])))
    events['Spring'] = sorted(list(set(events['Spring'])))

    return events

