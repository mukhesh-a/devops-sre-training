"""
Python Control Flow Demo - For DevOps Interns
=============================================
Covers: if/elif/else, for loops, while loops
"""

print("=" * 60)
print("PYTHON CONTROL FLOW - IF/ELSE, FOR, WHILE")
print("=" * 60)

# =============================================================================
# 1. IF / ELIF / ELSE
# =============================================================================
print("\n--- 1. IF / ELIF / ELSE ---")

# Simple if
status_code = 200
if status_code == 200:
    print(f"  status_code {status_code} -> OK")

# if / else
status_code = 404
if status_code == 200:
    print("  OK")
else:
    print(f"  status_code {status_code} -> Not OK")

# if / elif / else (multiple conditions)
status_code = 503
if status_code == 200:
    print("  OK")
elif status_code == 404:
    print("  Not Found")
elif status_code in (500, 502, 503):
    print("  Server Error")
else:
    print("  Other status")

# Truthiness and comparison
disk_usage_percent = 85
if disk_usage_percent > 90:
    print("  Disk: CRITICAL")
elif disk_usage_percent > 80:
    print("  Disk: WARNING")
else:
    print("  Disk: OK")

# Combining conditions (and, or, not)
port = 443
is_ssl = True
if port == 443 and is_ssl:
    print("  HTTPS connection")

env = "production"
if env == "production" or env == "staging":
    print("  Non-dev environment")

# =============================================================================
# 2. FOR LOOPS
# =============================================================================
print("\n" + "-" * 60)
print("--- 2. FOR LOOPS ---")

# Loop over a list
servers = ["web-01", "web-02", "db-01"]
print("  Iterating over list:")
for server in servers:
    print(f"    - {server}")

# Loop with index: enumerate()
print("\n  With index (enumerate):")
for index, server in enumerate(servers):
    print(f"    [{index}] {server}")

# Loop over a dictionary
config = {"host": "0.0.0.0", "port": 8080, "debug": False}
print("\n  Iterating over dict (keys):")
for key in config:
    print(f"    {key} = {config[key]}")

print("  Iterating over dict (items):")
for key, value in config.items():
    print(f"    {key} = {value}")

# Loop over a range
print("\n  range(5):")
for i in range(5):
    print(f"    i = {i}", end="  ")
print()

print("  range(2, 6):")
for i in range(2, 6):
    print(f"    i = {i}", end="  ")
print()

# Loop with break (stop early)
print("\n  break when found:")
for name in ["alpha", "beta", "gamma", "delta"]:
    if name == "gamma":
        print(f"    Found: {name}")
        break
    print(f"    Checking {name}...")

# Loop with continue (skip iteration)
print("\n  continue (skip even numbers):")
for n in range(1, 7):
    if n % 2 == 0:
        continue
    print(f"    Odd: {n}")

# =============================================================================
# 3. WHILE LOOPS
# =============================================================================
print("\n" + "-" * 60)
print("--- 3. WHILE LOOPS ---")

# Basic while (run until condition is False)
count = 0
print("  Count up to 3:")
while count < 3:
    print(f"    count = {count}")
    count += 1
print(f"  Done. count = {count}")

# Simulate retries (common in DevOps)
max_retries = 3
attempt = 0
print("\n  Retry simulation:")
while attempt < max_retries:
    attempt += 1
    print(f"    Attempt {attempt}/{max_retries}")
    if attempt == 2:
        print("      Success!")
        break
else:
    # while-else: runs if loop ends without break
    print("    All retries exhausted.")

# While with user/condition (example: polling until ready)
ready = False
polls = 0
print("\n  Polling until ready (max 3):")
while not ready and polls < 3:
    polls += 1
    print(f"    Poll {polls}...")
    if polls == 2:
        ready = True
        print("    Service is ready.")
if not ready:
    print("    Timeout.")

# =============================================================================
# QUICK REFERENCE
# =============================================================================
print("\n" + "=" * 60)
print("QUICK REFERENCE")
print("=" * 60)
print("""
  if / elif / else  -> one path based on condition
  for x in iterable   -> loop over list, dict, range, etc.
  while condition    -> loop until condition is False
  break              -> exit loop immediately
  continue           -> skip to next iteration
  else (on loop)     -> runs if loop ends normally (no break)
""")
print("Done.")
