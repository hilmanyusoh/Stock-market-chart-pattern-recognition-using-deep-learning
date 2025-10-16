from scipy.signal import find_peaks
import numpy as np
import pandas as pd

def detect_head_shoulders(df, distance=5, tolerance=0.03, debug=False):
    prices = df['close'].values
    peaks, _ = find_peaks(prices, distance=distance)
    troughs, _ = find_peaks(-prices, distance=distance)
    
    patterns = []

    # Head & Shoulders
    for i in range(2, len(peaks)):
        l, h, r = peaks[i-2], peaks[i-1], peaks[i]
        left, head, right = prices[l], prices[h], prices[r]
        if head > left and head > right and abs(left - right)/head < tolerance:
            patterns.append({
                "type": "H&S",
                "left_idx": l,
                "head_idx": h,
                "right_idx": r
            })

    # Inverse Head & Shoulders
    for i in range(2, len(troughs)):
        l, h, r = troughs[i-2], troughs[i-1], troughs[i]
        left, head, right = prices[l], prices[h], prices[r]
        if head < left and head < right and abs(left - right)/head < tolerance:
            patterns.append({
                "type": "IH&S",
                "left_idx": l,
                "head_idx": h,
                "right_idx": r
            })

    return patterns


