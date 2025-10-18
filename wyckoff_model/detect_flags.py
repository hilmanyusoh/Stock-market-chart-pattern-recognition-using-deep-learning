import pandas as pd
import numpy as np

def detect_flag_patterns(df: pd.DataFrame, 
                         pole_length_ratio: float = 0.10, 
                         flag_duration_max: int = 30, 
                         flag_slope_max: float = 0.3) -> list:
    """
    ฟังก์ชันสำหรับตรวจจับรูปแบบ Bullish Flag และ Bearish Flag
    """

    prices = df['close'].values
    n = len(prices)
    patterns = []
    
    MIN_LENGTH = 50
    if n < MIN_LENGTH:
        return patterns

    for i in range(MIN_LENGTH, n):
        pole_start_idx = i - 20 # 20 แท่งสำหรับ Pole
        pole_end_idx = i
        pole_prices = prices[pole_start_idx:pole_end_idx]
        
        high_price = np.max(pole_prices)
        low_price = np.min(pole_prices)
        
        # ==================== BULLISH FLAG DETECTION ====================
        
        # 1. Bullish Pole: ขึ้นเร็ว (อย่างน้อย 10%)
        if (prices[pole_end_idx - 1] - prices[pole_start_idx]) / prices[pole_start_idx] > pole_length_ratio:
            
            # 2. Flag: หาช่วงพักตัว
            for flag_end_idx in range(pole_end_idx + 5, min(n, pole_end_idx + flag_duration_max)):
                
                flag_prices = prices[pole_end_idx:flag_end_idx]
                flag_length = len(flag_prices)
                
                if flag_length < 5: continue 

                flag_high = np.max(flag_prices)
                flag_low = np.min(flag_prices)
                slope = (flag_prices[-1] - flag_prices[0]) / flag_length
                
                # เงื่อนไข: 1) กรอบแคบ 2) ความชันเป็นลบ (สวนทาง)
                if ((flag_high - flag_low) < (high_price - low_price) / 3 and 
                    slope < 0 and 
                    abs(slope) < flag_slope_max):
                    
                    # 3. Breakout: แท่งถัดไปต้องสูงกว่า Flag High
                    if flag_end_idx + 1 < n and prices[flag_end_idx + 1] > flag_high:
                        patterns.append({
                            "type": "Bullish Flag",
                            "pole_start_idx": pole_start_idx,
                            "pole_end_idx": pole_end_idx,
                            "flag_start_idx": pole_end_idx,
                            "flag_end_idx": flag_end_idx,
                            "breakout_idx": flag_end_idx + 1
                        })
                        break 

        # ==================== BEARISH FLAG DETECTION ====================
        
        # 1. Bearish Pole: ลงเร็ว (อย่างน้อย 10%)
        if (prices[pole_start_idx] - prices[pole_end_idx - 1]) / prices[pole_start_idx] > pole_length_ratio:
            
            # 2. Flag: หาช่วงพักตัว
            for flag_end_idx in range(pole_end_idx + 5, min(n, pole_end_idx + flag_duration_max)):
                
                flag_prices = prices[pole_end_idx:flag_end_idx]
                flag_length = len(flag_prices)
                
                if flag_length < 5: continue

                flag_high = np.max(flag_prices)
                flag_low = np.min(flag_prices)
                slope = (flag_prices[-1] - flag_prices[0]) / flag_length
                
                # เงื่อนไข: 1) กรอบแคบ 2) ความชันเป็นบวก (สวนทาง)
                if ((flag_high - flag_low) < (high_price - low_price) / 3 and 
                    slope > 0 and 
                    slope < flag_slope_max):
                    
                    # 3. Breakout: แท่งถัดไปต้องต่ำกว่า Flag Low
                    if flag_end_idx + 1 < n and prices[flag_end_idx + 1] < flag_low:
                        patterns.append({
                            "type": "Bearish Flag",
                            "pole_start_idx": pole_start_idx,
                            "pole_end_idx": pole_end_idx,
                            "flag_start_idx": pole_end_idx,
                            "flag_end_idx": flag_end_idx,
                            "breakout_idx": flag_end_idx + 1
                        })
                        break 

    return patterns