with open('/root/oshi-trader/main.py', 'r') as f:
    content = f.read()

# Fix the broken telegram comment
old_block = '''                            # DISABLED: await self.telegram.notify_exit(
                                asset="BTC" if "BTC" in ticker else "SOL",
                                direction=trade.direction,
                                entry_price=trade.entry_price,
                                exit_price=current_price,
                                pnl=pnl,
                                exit_reason="TAKE_PROFIT",
                                balance=self.balance
                            )'''

new_block = '''                            # Telegram notification DISABLED
                            pass'''

if old_block in content:
    content = content.replace(old_block, new_block)
    print("Fixed broken telegram block")
else:
    print("Could not find broken telegram block")
    # Try to find any partial blocks
    if 'DISABLED: await self.telegram.notify_exit' in content:
        print("Found partial block, attempting manual fix...")
        # Comment out lines individually
        lines = content.split('\n')
        new_lines = []
        in_broken_block = False
        for line in lines:
            if 'DISABLED: await self.telegram.notify_exit' in line:
                in_broken_block = True
                new_lines.append('                            # Telegram DISABLED: notify_exit call removed')
            elif in_broken_block and line.strip() == ')':
                in_broken_block = False
                new_lines.append('')  # Skip the closing paren
            elif in_broken_block:
                new_lines.append('                            # ' + line.lstrip())
            else:
                new_lines.append(line)
        content = '\n'.join(new_lines)
        print("Fixed with line-by-line comment")

with open('/root/oshi-trader/main.py', 'w') as f:
    f.write(content)

print("Syntax fix applied!")
