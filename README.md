# Shirayuki System Medic - T1/T2 Strategy Documentation

🏥 **System Medic workspace with complete Kalshi trading strategy documentation**

## 🎯 Strategy Overview

This repository contains the complete technical specification for the **v11.0 "Trend-First"** Kalshi trading strategy, featuring:

### **T1 Strategy:** Trend + Confluence
- **Logic:** 15m trend + ≥2/4 confluence indicators  
- **Win Rate:** ~68% (trend-following edge)
- **Confluence:** PSAR + RSI + Momentum + Bollinger Bands

### **T2 Strategy:** Momentum Override  
- **Logic:** Strong 1h momentum ≥0.05% (can override NEUTRAL trend)
- **Win Rate:** 100% on launch day (4/4 trades)
- **Total Profit:** +$121.95 first day

## 📊 Performance Metrics

**Launch Day Results (2026-02-24):**
- **Balance:** $41.11 → $280.77 (~600% gain)  
- **Code Simplification:** 1900 → 735 lines (61% reduction)
- **T2 Perfect Record:** 4 consecutive successful trades

## 📋 Documentation

### **Main Strategy Document**
- **[KALSHI_T1_T2_STRATEGY.md](KALSHI_T1_T2_STRATEGY.md)** - Complete technical specification

### **Key Components:**
- **Tier Definitions:** T1 vs T2 entry criteria
- **Confluence System:** 4-indicator confirmation system  
- **Timing Windows:** Precise scan and entry windows
- **Position Sizing:** Compounding and risk management
- **Live Configuration:** Current server parameters and thresholds

## 🔧 Technical Details

### **4-Indicator Confluence System:**
1. **PSAR** - Trend direction confirmation
2. **RSI** - Oversold/overbought levels (35/65)  
3. **Momentum** - 5-min price change (±0.05%)
4. **Bollinger Bands** - Price position relative to bands

### **Timing Precision:**
- **Scan Window:** 12-9 minutes before expiration
- **Entry Window:** 12-8 minutes before expiration  
- **Take Profit:** Automatic at 89¢ regardless of entry

### **Compounding Logic:**
- **Base:** $50 → $100 after win → Reset after 2 wins
- **Max Size:** $100 per trade
- **Reset:** Any loss returns to $50 base

## 🚀 Live System

**Server:** 209.38.37.63  
**Service:** `kalshi-trader.service`  
**Status:** ACTIVE & PROVEN  
**Version:** v11.0 "Trend-First" (735 lines)

---

**Maintained by:** Shirayuki (System Medic)  
**Last Updated:** 2026-02-24  
**Repository:** Complete strategy documentation and technical specifications