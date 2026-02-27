import json

# Load all corrected trades
trades = []
with open('/root/oshi-trader/data/t2_trades.jsonl', 'r') as f:
    for line in f:
        if line.strip():
            try:
                trades.append(json.loads(line))
            except:
                pass

completed = [t for t in trades if t.get('outcome')]

print('='*120)
print('CORRECTED FINAL REPORT - ALL TRADES RESOLVED')
print('='*120)
print()

# Overall stats
wins = sum(1 for t in completed if t['outcome'] == 'TP')
losses = len(completed) - wins
total_pnl = sum(t.get('pnl', 0) or 0 for t in completed)
win_pnl = sum(t.get('pnl', 0) or 0 for t in completed if t['outcome'] == 'TP')
loss_pnl = sum(t.get('pnl', 0) or 0 for t in completed if t['outcome'] == 'LOSS')

print('FINAL PERFORMANCE SUMMARY')
print('-'*120)
print(f'Total Trades: {len(completed)}')
print(f'Wins: {wins}')
print(f'Losses: {losses}')
print(f'Win Rate: {wins/len(completed)*100:.1f}%')
print(f'Total PnL: ${total_pnl:+.2f}')
print(f'Win PnL: ${win_pnl:+.2f}')
print(f'Loss PnL: ${loss_pnl:+.2f}')
if wins > 0:
    print(f'Avg Win: ${win_pnl/wins:.2f}')
if losses > 0:
    print(f'Avg Loss: ${loss_pnl/losses:.2f}')
print()

# Detailed table
print('COMPLETE TRADE DATA TABLE')
print('-'*120)

for i, t in enumerate(completed, 1):
    ts = t.get('timestamp', 'N/A')
    if 'T' in str(ts):
        ts = ts.split('T')[0][5:] + ' ' + ts.split('T')[1][:5]
    
    ticker_short = t.get('ticker', 'N/A').replace('KXBTC15M-', '')
    direction = t.get('direction', '?')
    entry = f"{t.get('entry_price', 0)}c"
    bet = f"${t.get('btc_bet', 0):.0f}"
    trend = t.get('trend_15m', 'N/A')
    mom = f"{t.get('momentum_1h', 0):+.2f}%"
    
    ind = t.get('indicators', {})
    rsi = f"{ind.get('rsi', 0):.0f}" if ind else 'N/A'
    psar = ind.get('psar', 'N/A') if ind else 'N/A'
    
    confl = f"{t.get('confluence', 0)}/4"
    outcome = 'WIN' if t['outcome'] == 'TP' else 'LOSS'
    pnl = f"${t.get('pnl', 0):+.2f}"
    
    print(f'{i:>3} | {ts:<14} | {ticker_short:<20} | {direction:<4} | {entry:<6} | {bet:<6} | {trend:<10} | {mom:<9} | {rsi:<5} | {psar:<7} | {confl:<5} | {outcome:<6} | {pnl:<9}')

print('-'*120)
print()
print('KEY INSIGHTS:')
print(f'  - Strategy win rate: {wins/len(completed)*100:.1f}% (target ~67%)')
print(f'  - Net profit: ${total_pnl:+.2f} on {len(completed)} trades')
if wins and losses:
    print(f'  - Risk/Reward ratio: {abs((win_pnl/wins) / (loss_pnl/losses)):.2f}')
print()
print('CORRECTIONS MADE:')
print('  - Fixed 2 trades: Found TP HIT in logs, marked as WIN')
print('  - Fixed 8 trades: No resolution found, marked as expired LOSS')
