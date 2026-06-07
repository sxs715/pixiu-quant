# 貔貅量化 | PixiuQuant

**专业加密货币量化交易系统 — EMA144多时间框架共振 + 递增加仓 + 阶梯止盈**

👉 实盘网站: [pixiu-ai.cn](https://pixiu-ai.cn)

## 核心特性

- 🎯 **EMA144 趋势跟踪** — 多时间框架共振信号，捕捉趋势启动点
- 📈 **多空双向** — 独立扫描、独立开仓，做多做空互不干扰
- 📊 **信号评分系统** — 全量扫描 TOP100 币种，多维度打分择优开仓
- 🔒 **阶梯止盈** — TP1/TP2/TP3 分级锁仓，利润最大化
- ⚡ **0.1秒风控** — 独立监控线程，止损/追踪止盈实时执行
- 🧠 **递增加仓** — 6级余额分档，盈冲亏缩自适应仓位

## 策略框架

```python
# 入场条件（做多）
# 1. 15m K线 收盘 > EMA144
# 2. EMA144 斜率向上（12周期）
# 3. 当前K线为阴线（回调买入）
# 4. 成交量 > 20周期均量 × 1.5
# 5. 日线过滤：EMA20多头排列 + RSI < 75
```

```
# 出场规则
# TP1: 盈亏 25% → 平 20% 仓位 + 锁仓利润 5%
# TP2: 盈亏 50% → 平 30% 仓位 + 启动追踪止盈
# TP3: 盈亏 75% → 阶梯推保护
# SL:  亏损 30% → 全平止损
# 超时: 持仓 45 分钟 → 全平
```

## 技术栈

- **Python 3** + **asyncio** 异步架构
- **ccxt** 交易所统一接口
- **numpy** 指标计算
- Binance Futures API
- Telegram Bot 远程控制

## 链接

- 🏠 官网: [pixiu-ai.cn](https://pixiu-ai.cn)
- 📊 实时信号: [pixiu-ai.cn/signals](https://pixiu-ai.cn/signals)
- ⚔️ 实盘战场: [pixiu-ai.cn/v10](https://pixiu-ai.cn/v10)
- 🧪 策略训练: [pixiu-ai.cn/sim](https://pixiu-ai.cn/sim)

## License

MIT © 貔貅量化

## 📊 实盘战绩（实时更新）

> 完整实盘数据: [pixiu-ai.cn/v10](https://pixiu-ai.cn/v10)

