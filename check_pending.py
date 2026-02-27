import json

# Load all trades
trades = []
with open('/root/oshi-trader/data/t2_trades.jsonl', 'r') as f:
    for line in f:
        if line.strip():
            try:
                trades.append(json.loads(line))
            except:
                pass

# Find pending trades
pending = [t for t in trades if not t.get('outcome') or t.get('outcome') == 'null']

print('='*100)
print('PENDING TRADES AUDIT')
print('='*100)
print(f"\nFound {len(pending)} pending trades:\n")

for t in pending:
    print(f"Ticker: {t.get('ticker')}")
    print(f"  Time: {t.get('timestamp')}")
    print(f"  Direction: {t.get('direction')}")
    print(f"  Entry: {t.get('entry_price')}c")
    print(f"  Contracts: {t.get('contracts')}")
    print(f"  Cost: ${t.get('cost')}")
    print()

# Also check for these tickers in the main log
print('='*100)
print('CHECKING TRADER LOG FOR RESOLUTIONS')
print('='*100)
print()

with open('/root/oshi-trader/data/trader.log', 'r') as f:
    log_content = f.read()

for t in pending:
    ticker = t.get('ticker', '')
    if ticker in log_content:
        # Check for TP or SETTLED
        if f'TP HIT]{ticker}' in log_content or f'TP HIT] {ticker}' in log_content:
            print(f"{ticker}: FOUND TP HIT IN LOG - Should be marked as WIN")
        elif f'SETTLED] {ticker}' in log_content:
            print(f"{ticker}: FOUND SETTLED IN LOG - Should be marked as LOSS")
        else:
            print(f"{ticker}: No resolution found in recent logs")
    else:
        print(f"{ticker}: Not found in log (old trade)")
