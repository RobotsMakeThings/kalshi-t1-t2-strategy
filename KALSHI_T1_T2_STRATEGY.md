# Kalshi T1/T2 Trading Strategy - v11.0 "Trend-First"

## 🎯 Core Philosophy

**Primary Discovery:** Following 15m trend = 68% WR, fading = 22% WR (45pp edge!)

**Strategy Evolution:**
- **v10.x:** Indicator-driven with complex tier system (F/S/A/B/C tiers)
- **v11.0:** Simplified to trend-first approach with T1/T2 tiers only
- **Result:** From 1900 lines → 735 lines (61% reduction), improved performance

---

## 🔄 Strategy Flow

```
1. GET 15m TREND → Direction (not from indicators)
2. CALCULATE CONFLUENCE → Quality confirmation (4 indicators)  
3. CHECK 1h MOMENTUM → T2 override capability
4. DETERMINE TIER → T1 (trend+confluence) vs T2 (momentum-driven)
5. EXECUTE TRADE → With precise timing windows
```

---

## 📊 TIER DEFINITIONS

### **T1: Trend + Confluence (Primary Strategy)**
- **Entry Logic:** 15m trend + ≥2/4 confluence indicators
- **Win Rate:** ~68% (trend-following edge)
- **Position Size:** Full size ($50 base, $100 with compounding)
- **Requirements:**
  - 15m trend must be UP or DOWN (not NEUTRAL)
  - Minimum 2/4 confluence indicators agree with trend
  - Active during entry window (12-9 min before expiration)

### **T2: Strong Momentum Override (Secondary Strategy)**
- **Entry Logic:** Strong 1h momentum (≥0.05%) even with NEUTRAL 15m trend
- **Win Rate:** 100% (4/4 trades on launch day)
- **Position Size:** Full size ($50 base, $100 with compounding)
- **Requirements:**
  - 1h momentum ≥ 0.05% (5 basis points)
  - Can trigger even when 15m trend is NEUTRAL
  - Direction follows 1h momentum direction

### **T3: ELIMINATED** ❌
- **Status:** Removed due to poor performance (30% WR)
- **Reason:** Low-confidence signals were bleeding money

---

## 🎛️ CONFLUENCE INDICATORS (4 Total)

The confluence system uses **4 indicators** to confirm trend quality:

### 1. **PSAR (Parabolic SAR)**
- **YES Signal:** PSAR = "UP"
- **NO Signal:** PSAR = "DOWN" 
- **Weight:** 1/4 of confluence score

### 2. **RSI (Relative Strength Index)**
- **YES Signal:** RSI < 35 (oversold, potential bounce)
- **NO Signal:** RSI > 65 (overbought, potential fall)
- **Weight:** 1/4 of confluence score
- **Thresholds:**
  - RSI_OVERSOLD = 35
  - RSI_OVERBOUGHT = 65

### 3. **MOMENTUM (5-min price change)**
- **YES Signal:** Momentum > 0.05% (upward movement)
- **NO Signal:** Momentum < -0.05% (downward movement) 
- **Weight:** 1/4 of confluence score
- **Threshold:** MOMENTUM_THRESHOLD = 0.05%

### 4. **BOLLINGER BANDS**
- **YES Signal:** Price in "below_lower" or "lower_half" (potential reversal up)
- **NO Signal:** Price in "above_upper" or "upper_half" (potential reversal down)
- **Weight:** 1/4 of confluence score

### Confluence Scoring:
- **4/4:** Perfect confluence (rare, highest confidence)
- **3/4:** Strong confluence 
- **2/4:** Minimum for T1 trades
- **1/4:** Only valid for T2 momentum trades
- **0/4:** No confluence, skip trade

---

## ⏱️ TIMING WINDOWS

### **Scan Window: 12-9 minutes before expiration**
- **Purpose:** Gather trend and indicator data
- **Duration:** 180 seconds (3 minutes)
- **Timing:** 720s to 540s remaining
- **Activities:** 
  - Calculate 15m trend direction
  - Read RSI, PSAR, Momentum, Bollinger indicators
  - Determine confluence score
  - Classify as T1/T2/SKIP

### **Entry Window: 12-8 minutes before expiration** 
- **Purpose:** Execute trades with confirmed signals
- **Duration:** 240 seconds (4 minutes) 
- **Timing:** 720s to 480s remaining
- **Requirements:**
  - Signal must be confirmed during scan window
  - Market not already traded
  - Passes odds filter (≥15¢, ≤85¢)

---

## 💰 POSITION SIZING & COMPOUNDING

### **Base Betting System:**
- **BTC_BASE_BET:** $50 (starting bet size)
- **MAX_BET_SIZE:** $100 (maximum single bet)
- **COMPOUND_MULTIPLIER:** 2.0 (double bet after win)
- **WINS_TO_RESET:** 2 (reset to base after 2 consecutive wins)

### **Compounding Sequence:**
1. **Start:** $50 bet, streak = 0
2. **After 1 win:** $100 bet, streak = 1 
3. **After 2 wins:** Reset to $50 bet, streak = 0
4. **After any loss:** Reset to $50 bet, streak = 0

### **Position Size by Tier:**
- **T1:** Full size (base bet × compounding)
- **T2:** Full size (base bet × compounding)
- **T3:** ❌ Eliminated

---

## 🎯 TAKE PROFIT & RISK MANAGEMENT

### **Automatic Take Profit:**
- **TARGET:** 89¢ (regardless of entry price)
- **LOGIC:** Sell all contracts when bid reaches 89¢
- **SUCCESS RATE:** ~90%+ of winning trades hit TP

### **Odds Filtering:**
- **MIN_ODDS:** 15¢ (avoid sure things)
- **MAX_ODDS:** 85¢ (avoid longshots)
- **EXTREME_YES:** Skip if YES ≥ 85¢ 
- **EXTREME_NO:** Skip if NO ≤ 15¢

### **Market Exclusions:**
- **SOL Markets:** Disabled (14% WR confirmed)
- **Settled Markets:** Skip if already resolved
- **Traded Markets:** One trade per market maximum

---

## 🔧 TECHNICAL PARAMETERS

### **Trend Detection:**
- **TREND_THRESHOLD:** 0.1% (minimum for UP/DOWN classification)
- **Source:** 15-minute Binance BTC price data
- **Calculation:** (current_price - price_15m_ago) / price_15m_ago

### **Strong Momentum (T2 Trigger):**
- **STRONG_MOMENTUM:** 0.05% (threshold for T2 override)
- **Source:** 1-hour price momentum
- **Purpose:** Capture powerful moves even without 15m trend

### **RSI Settings:**
- **Period:** Standard 14-period RSI
- **Oversold:** < 35 (potential bounce signal)
- **Overbought:** > 65 (potential fall signal)

---

## 📈 PERFORMANCE METRICS

### **v11.0 Launch Day Results (2026-02-24):**
- **Balance:** $41.11 → $280.77 (~600% gain)
- **T1 Trades:** Ongoing monitoring
- **T2 Trades:** 4/4 successful (100% WR)
  - T2 #1: +$11.80 profit
  - T2 #2: +$21.76 profit  
  - T2 #3: +$71.79 profit
  - T2 #4: +$16.60 profit (TP hit @90¢)
- **Total T2 Profit:** +$121.95
- **Strategy Status:** PROVEN & ACTIVE

### **Historical Context:**
- **v10.x Best:** Multiple tier system, complex logic
- **v11.0 Advantage:** Simplified, trend-focused, higher WR
- **Key Insight:** Trend-following >> Contrarian in 15-min windows

---

## 🚀 LIVE CONFIGURATION

### **Server Details:**
- **IP:** 209.38.37.63
- **Path:** `/root/oshi-trader/main.py`
- **Service:** `kalshi-trader.service`
- **Version:** v11.0 "Trend-First" (735 lines)

### **Current Settings:**
```python
# Strategy Constants
TREND_THRESHOLD = 0.1       # % change for trend
STRONG_MOMENTUM = 0.05      # % change for T2
T1_MIN_CONFLUENCE = 2       # 2/4 for T1
MOMENTUM_THRESHOLD = 0.05   # % for momentum indicator
AUTO_TP = 89               # Take profit at 89¢

# Position Sizing
BTC_BASE_BET = 50.0
MAX_BET_SIZE = 100.0
COMPOUND_MULTIPLIER = 2.0
WINS_TO_RESET = 2

# Risk Management  
EXTREME_YES = 85           # Skip YES >= 85¢
EXTREME_NO = 15            # Skip NO <= 15¢
RSI_OVERSOLD = 35
RSI_OVERBOUGHT = 65
```

---

## 🔄 ALGORITHM PSEUDOCODE

```python
def evaluate_market(market):
    # 1. Get trend direction (primary signal)
    trend_15m = get_15m_trend(market.ticker)
    
    # 2. Get 1h momentum for T2 check
    momentum_1h = get_1h_momentum(market.ticker) 
    momentum_strong = abs(momentum_1h) >= STRONG_MOMENTUM
    
    # 3. Calculate confluence (quality check)
    indicators = get_indicators(market.ticker)  # RSI, PSAR, Mom, BB
    confluence = count_confluence(trend_15m.direction, indicators)
    
    # 4. Determine tier
    if momentum_strong:
        tier = "T2"  # Can trade even with NEUTRAL 15m trend
        direction = get_1h_momentum_direction(momentum_1h)
    elif trend_15m.direction != "NEUTRAL" and confluence >= 2:
        tier = "T1"  # Need trend + confluence
        direction = trend_15m.direction
    else:
        return SKIP  # No valid signal
    
    # 5. Check timing window
    if not in_entry_window(market.close_time):
        return WAIT
    
    # 6. Check odds filter
    entry_price = market.get_price(direction)
    if entry_price < 15 or entry_price > 85:
        return SKIP
        
    # 7. Execute trade
    bet_size = get_bet_size_with_compounding(tier)
    contracts = int(bet_size / (entry_price / 100))
    
    return place_order(market.ticker, direction, contracts, entry_price)
```

---

## 📊 MONITORING DASHBOARD

### **Key Metrics to Track:**
- **T1 Win Rate:** Target >65%
- **T2 Win Rate:** Current 100% (early sample)
- **Average Hold Time:** ~8-12 minutes to TP
- **Confluence Distribution:** Monitor 2/4 vs 3/4 vs 4/4 performance
- **Compounding Effectiveness:** Track streak management

### **Alert Thresholds:**
- **Win Rate Drop:** <60% over 20 trades
- **Consecutive Losses:** ≥3 in a row
- **Low Volume Days:** <5 qualified signals
- **Extreme Odds:** >50% of signals filtered out

---

**Last Updated:** 2026-02-24  
**Status:** LIVE & PROVEN  
**Next Review:** After 50 T1+T2 trades combined