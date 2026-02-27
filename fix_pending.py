import json

# Update the enhanced log file
with open('/root/oshi-trader/data/t2_trades.jsonl', 'r') as f:
    lines = f.readlines()

updated = []
for line in lines:
    if line.strip():
        try:
            trade = json.loads(line)
            ticker = trade.get('ticker', '')
            
            # Fix 242000-00
            if '26FEB242000-00' in ticker:
                trade['outcome'] = 'TP'
                trade['exit_price'] = 91
                trade['pnl'] = (91 - 61) * 81 / 100
                print(f'Updated {ticker}: WIN at 91c, PnL +${trade[\"pnl\"]:.2f}')
            
            # Fix 242100-00
            elif '26FEB242100-00' in ticker:
                trade['outcome'] = 'TP'
                trade['exit_price'] = 93
                trade['pnl'] = (93 - 60) * 166 / 100
                print(f'Updated {ticker}: WIN at 93c, PnL +${trade[\"pnl\"]:.2f}')
            
            updated.append(json.dumps(trade) + '\n')
        except:
            updated.append(line)

# Write back
with open('/root/oshi-trader/data/t2_trades.jsonl', 'w') as f:
    f.writelines(updated)

print('Done updating pending trades!')
