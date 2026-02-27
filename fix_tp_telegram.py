# Read the file
with open('/root/oshi-trader/main.py', 'r') as f:
    content = f.read()

# 1. DISABLE TELEGRAM ALERTS by commenting out all telegram calls
# Comment out telegram import and initialization
old_import = '''# Telegram notifications
from brains.telegram_notifier import TelegramNotifier'''

new_import = '''# Telegram notifications - DISABLED (broken)
# from brains.telegram_notifier import TelegramNotifier'''

if old_import in content:
    content = content.replace(old_import, new_import)
    print("✅ Commented out Telegram import")
else:
    print("⚠️  Could not find Telegram import")

# Comment out telegram initialization
old_init = '''        self.telegram = TelegramNotifier("Kalshi")'''

new_init = '''        # self.telegram = TelegramNotifier("Kalshi")  # DISABLED'''

if old_init in content:
    content = content.replace(old_init, new_init)
    print("✅ Commented out Telegram initialization")
else:
    print("⚠️  Could not find Telegram init")

# Comment out all telegram.notify_exit calls
content = content.replace('await self.telegram.notify_exit(', '# DISABLED: await self.telegram.notify_exit(')
content = content.replace('await self.telegram.notify_entry(', '# DISABLED: await self.telegram.notify_entry(')
print("✅ Commented out all Telegram notify calls")

# 2. ENHANCE TP CHECKING - Add more frequent position checks
# Update the run loop to check positions more frequently
old_loop = '''                # Check positions
                await self.check_positions()
                
                # Update balance
                self.balance = await self.kalshi.get_balance()
                
                # Heartbeat every 30s
                now = time.time()
                if now - last_heartbeat > 30:
                    self.print_heartbeat()
                    last_heartbeat = now
                
                await asyncio.sleep(10)'''

new_loop = '''                # Check positions MORE FREQUENTLY for TP (every 2 seconds, 5 times per loop)
                for _ in range(5):
                    await self.check_positions()
                    await asyncio.sleep(2)
                
                # Update balance
                self.balance = await self.kalshi.get_balance()
                
                # Heartbeat every 30s
                now = time.time()
                if now - last_heartbeat > 30:
                    self.print_heartbeat()
                    last_heartbeat = now
                
                await asyncio.sleep(0)  # Minimal sleep to yield control'''

if old_loop in content:
    content = content.replace(old_loop, new_loop)
    print("✅ Enhanced position checking to every 2 seconds")
else:
    print("⚠️  Could not find main loop to modify")

# 3. ADD AGGRESSIVE TP LOGGING
old_tp_check = '''                # Check take profit at 88¢
                if current_price >= AUTO_TP:'''

new_tp_check = '''                # AGGRESSIVE TP CHECKING - Log every check
                logger.info(f"[TP CHECK] {ticker}: {side} @ {current_price}¢ vs target {AUTO_TP}¢ | Position: {position}")
                
                # Check take profit at 89¢
                if current_price >= AUTO_TP:'''

if old_tp_check in content:
    content = content.replace(old_tp_check, new_tp_check)
    print("✅ Added aggressive TP logging")
else:
    print("⚠️  Could not find TP check to enhance")

# Write the file
with open('/root/oshi-trader/main.py', 'w') as f:
    f.write(content)

print("\n✅ Changes applied:")
print("  1. Telegram alerts DISABLED")
print("  2. Position/TP checking every 2 seconds (was 10s)")
print("  3. TP check logging added for debugging")
print("\nTP will now be checked every 2 seconds and logged every time!")
