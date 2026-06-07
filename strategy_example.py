#!/usr/bin/env python3
"""
貔貅量化 — EMA144 多空策略示例
仅供参考，完整系统请访问 pixiu-ai.cn
"""
import numpy as np

def ema(arr, span):
    """指数移动平均"""
    if len(arr) == 0:
        return np.array([])
    alpha = 2 / (span + 1)
    result = np.zeros_like(arr)
    result[0] = arr[0]
    for i in range(1, len(arr)):
        result[i] = alpha * arr[i] + (1 - alpha) * result[i - 1]
    return result

def rsi(close, period=14):
    """相对强弱指标"""
    if len(close) < period + 1:
        return np.nan
    deltas = np.diff(close)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])
    if avg_loss == 0:
        return 100.0
    for i in range(period, len(deltas)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def check_entry_long(close, open_, high, low, volume):
    """EMA144 趋势做多入场信号"""
    e144 = ema(close, 144)
    slope = e144[-1] - e144[-13]  # 12周期斜率
    
    # 价格在 EMA144 上方
    if close[-1] <= e144[-1]:
        return False, 0
    # EMA144 斜率向上
    if slope <= 0:
        return False, 0
    # 当前K线为阴线（回调买入）
    if close[-1] >= open_[-1]:
        return False, 0
    # 放量过滤
    avg_vol = np.mean(volume[-21:-1])
    vol_ratio = volume[-1] / avg_vol if avg_vol > 0 else 0
    if vol_ratio < 1.5:
        return False, 0
    
    # 信号评分 (满分100)
    deviation = min((close[-1] - e144[-1]) / e144[-1] / 0.02, 1.0) * 35
    slope_score = min(abs(slope) / close[-1] / 0.001, 1.0) * 25
    vol_score = min((vol_ratio - 1.5) / 1.5, 1.0) * 20
    
    score = deviation + slope_score + vol_score
    return True, round(score, 1)

if __name__ == "__main__":
    print("貔貅量化 EMA144 策略框架 v10.0")
    print("完整系统: https://pixiu-ai.cn")
