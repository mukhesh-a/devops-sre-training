"""
Python Collections Demo - For DevOps Interns
============================================
Covers: Lists, Dictionaries, Tuples, and Sets
"""

print("=" * 60)
print("PYTHON COLLECTIONS - LISTS, DICTIONARIES, TUPLES, SETS")
print("=" * 60)

# =============================================================================
# 1. LISTS - Ordered, Mutable, Allows Duplicates
# =============================================================================
print("\n--- 1. LISTS ---")
print("Ordered, mutable, allows duplicates. Use [ ]")

# Creating a list
servers = ["web-01", "web-02", "db-01", "cache-01", "web-01"]
ports = [80, 443, 3306, 6379]

print(f"servers = {servers}")
print(f"ports   = {ports}")

# Accessing list elements (zero-indexed)
print("\nAccessing by index:")
print(f"  servers[0]     = {servers[0]}")       # First element
print(f"  servers[-1]    = {servers[-1]}")      # Last element
print(f"  servers[1:3]   = {servers[1:3]}")     # Slice: index 1 to 2
print(f"  servers[:2]    = {servers[:2]}")      # First two
print(f"  servers[-2:]   = {servers[-2:]}")     # Last two

# Common list operations
servers.append("lb-01")
print(f"\nAfter append('lb-01'): {servers}")
print(f"Length: len(servers) = {len(servers)}")
print(f"Count 'web-01': servers.count('web-01') = {servers.count('web-01')}")

# =============================================================================
# 2. DICTIONARIES - Key-Value Pairs, Mutable
# =============================================================================
print("\n" + "-" * 60)
print("--- 2. DICTIONARIES ---")
print("Key-value pairs. Use { }")

# Creating a dictionary (like config / env vars)
config = {
    "app_name": "my-api",
    "port": 8080,
    "debug": False,
    "host": "0.0.0.0",
}

env_vars = {"DATABASE_URL": "postgres://localhost/db", "LOG_LEVEL": "INFO"}

print(f"config   = {config}")
print(f"env_vars = {env_vars}")

# Accessing dictionary elements
print("\nAccessing by key:")
print(f"  config['app_name']  = {config['app_name']}")
print(f"  config['port']      = {config['port']}")
print(f"  config.get('host')  = {config.get('host')}")
print(f"  config.get('missing', 'default') = {config.get('missing', 'default')}")

# Keys and values
print(f"\n  config.keys()   = {list(config.keys())}")
print(f"  config.values() = {list(config.values())}")
print(f"  config.items()  = {list(config.items())}")

# Add/update
config["workers"] = 4
print(f"\nAfter config['workers'] = 4: {config}")

# =============================================================================
# 3. TUPLES - Ordered, Immutable
# =============================================================================
print("\n" + "-" * 60)
print("--- 3. TUPLES ---")
print("Ordered, immutable. Use ( )")

# Creating tuples (good for fixed data: coordinates, (host, port), etc.)
server_endpoint = ("api.example.com", 443)
rgb_color = (255, 128, 0)
single = (1,)  # Single-element tuple needs trailing comma

print(f"server_endpoint = {server_endpoint}")
print(f"rgb_color       = {rgb_color}")
print(f"single          = {single}")

# Accessing tuple elements (same as list: index and slice)
print("\nAccessing by index:")
print(f"  server_endpoint[0]  = {server_endpoint[0]}")
print(f"  server_endpoint[1]  = {server_endpoint[1]}")
print(f"  rgb_color[1:]       = {rgb_color[1:]}")

# Unpacking
host, port = server_endpoint
print(f"\nUnpacking: host, port = server_endpoint")
print(f"  host = {host}, port = {port}")

# =============================================================================
# 4. SETS - Unordered, Mutable, No Duplicates
# =============================================================================
print("\n" + "-" * 60)
print("--- 4. SETS ---")
print("Unordered, unique elements only. Use { }")

# Creating a set (great for unique values: unique IPs, tags, etc.)
unique_ports = {80, 443, 8080, 80, 443}  # Duplicates removed
tags = set(["production", "us-east", "production"])

print(f"unique_ports = {unique_ports}")
print(f"tags         = {tags}")

# Accessing: sets are unordered, so no index like [0]
# Use: membership, iteration, or convert to list for order
print("\nAccessing (no index; use 'in' and iteration):")
print(f"  80 in unique_ports = {80 in unique_ports}")
print(f"  999 in unique_ports = {999 in unique_ports}")
print(f"  Iteration: ", end="")
for p in sorted(unique_ports):
    print(p, end=" ")
print()

# Set operations
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(f"\nSet operations: set_a = {set_a}, set_b = {set_b}")
print(f"  set_a | set_b (union)     = {set_a | set_b}")
print(f"  set_a & set_b (intersection) = {set_a & set_b}")
print(f"  set_a - set_b (difference)   = {set_a - set_b}")

# Add to set
unique_ports.add(3000)
print(f"\nAfter add(3000): unique_ports = {unique_ports}")

# =============================================================================
# QUICK REFERENCE SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("QUICK REFERENCE")
print("=" * 60)
print("""
  Collection   | Syntax  | Ordered | Mutable | Duplicates
  -------------|---------|---------|---------|------------
  List         | [ ]     | Yes     | Yes     | Yes
  Dictionary   | { }     | (keys)  | Yes     | No (keys)
  Tuple        | ( )     | Yes     | No      | Yes
  Set          | { }     | No      | Yes     | No
""")
print("Done.")
