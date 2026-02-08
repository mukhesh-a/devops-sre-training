"""
Python JSON Package Demo - For DevOps Interns
=============================================
Encode/decode JSON, iterate over values, read/write files.
Useful for configs, API responses, and automation.

No install needed: json is in the standard library.
"""

import json

print("=" * 60)
print("JSON PACKAGE - PARSING, DUMPING, ITERATION")
print("=" * 60)

# =============================================================================
# 1. STRING TO PYTHON (json.loads)
# =============================================================================
print("\n--- 1. json.loads() - STRING TO PYTHON ---")

json_string = '{"app": "api", "port": 8080, "env": "production"}'
data = json.loads(json_string)

print(f"  Input (str): {json_string}")
print(f"  Output type: {type(data)}")
print(f"  data['app']  = {data['app']}")
print(f"  data['port'] = {data['port']}")

# =============================================================================
# 2. PYTHON TO STRING (json.dumps)
# =============================================================================
print("\n--- 2. json.dumps() - PYTHON TO STRING ---")

config = {"host": "0.0.0.0", "port": 443, "ssl": True}
json_str = json.dumps(config)

print(f"  config (dict): {config}")
print(f"  json.dumps(config) = {json_str}")
print(f"  Type: {type(json_str)}")

# Pretty-print with indent
pretty = json.dumps(config, indent=2)
print("  With indent=2:")
print(pretty)

# =============================================================================
# 3. ITERATING OVER JSON VALUES (DICT)
# =============================================================================
print("\n--- 3. ITERATING OVER JSON (DICT) ---")

api_response = {
    "status": "ok",
    "services": ["web", "db", "cache"],
    "count": 3,
}

print("  By keys:")
for key in api_response:
    print(f"    key: {key} -> {api_response[key]}")

print("  By items (key, value):")
for key, value in api_response.items():
    print(f"    {key!r}: {value}")

print("  By values only:")
for value in api_response.values():
    print(f"    {value}")

# =============================================================================
# 4. ITERATING OVER JSON (LIST / ARRAY)
# =============================================================================
print("\n--- 4. ITERATING OVER JSON (LIST) ---")

servers = ["web-01", "web-02", "db-01"]
print(f"  servers = {servers}")

for index, server in enumerate(servers):
    print(f"    [{index}] {server}")

# List of dicts (e.g. API list response)
instances = [
    {"id": "i-001", "state": "running"},
    {"id": "i-002", "state": "stopped"},
]
print("  List of dicts:")
for instance in instances:
    print(f"    id: {instance['id']}, state: {instance['state']}")

# =============================================================================
# 5. NESTED JSON - ACCESS AND ITERATION
# =============================================================================
print("\n--- 5. NESTED JSON - ACCESS & ITERATION ---")

nested = {
    "region": "us-east-1",
    "vpc": {
        "id": "vpc-123",
        "subnets": ["subnet-a", "subnet-b"],
    },
    "tags": {"Env": "prod", "Team": "devops"},
}

print("  Access nested:")
print(f"    nested['vpc']['id']     = {nested['vpc']['id']}")
print(f"    nested['vpc']['subnets'] = {nested['vpc']['subnets']}")

print("  Iterate nested dict:")
for tag_key, tag_value in nested["tags"].items():
    print(f"    tag: {tag_key} = {tag_value}")

print("  Iterate nested list:")
for subnet in nested["vpc"]["subnets"]:
    print(f"    subnet: {subnet}")

# =============================================================================
# 6. READ FROM FILE (json.load)
# =============================================================================
print("\n--- 6. json.load() - READ FROM FILE ---")

# Write a temp file for demo, then read
demo_config = {"timeout": 30, "retries": 3}
config_path = "demo_config.json"

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(demo_config, f, indent=2)
print(f"  Wrote {config_path}")

with open(config_path, encoding="utf-8") as f:
    loaded = json.load(f)
print(f"  json.load(f) -> {loaded}")

# =============================================================================
# 7. WRITE TO FILE (json.dump)
# =============================================================================
print("\n--- 7. json.dump() - WRITE TO FILE ---")

output = {"servers": ["web-01", "db-01"], "updated": True}
output_path = "demo_output.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
print(f"  json.dump(data, f, indent=2) -> {output_path}")

# =============================================================================
# 8. USEFUL OPTIONS
# =============================================================================
print("\n--- 8. USEFUL OPTIONS ---")

# sort_keys: stable key order
data_unsorted = {"z": 1, "a": 2, "m": 3}
print("  sort_keys=True:")
print(f"    {json.dumps(data_unsorted, sort_keys=True)}")

# ensure_ascii: keep non-ASCII as-is when False
text_with_unicode = {"message": "café", "note": "naïve"}
print("  ensure_ascii=False:")
print(f"    {json.dumps(text_with_unicode, ensure_ascii=False)}")

# =============================================================================
# 9. ITERATING DEEPLY (WALK ALL VALUES)
# =============================================================================
print("\n--- 9. WALK ALL VALUES (RECURSIVE-STYLE) ---")


def print_json_values(obj, prefix=""):
    """Iterate over all values in a JSON-like structure (dict/list)."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"    {prefix}{k!r}: ", end="")
            if isinstance(v, (dict, list)):
                print()
                print_json_values(v, prefix + "  ")
            else:
                print(f"{v!r}")
    elif isinstance(obj, list):
        for i, elem in enumerate(obj):
            print(f"    {prefix}[{i}]: ", end="")
            if isinstance(elem, (dict, list)):
                print()
                print_json_values(elem, prefix + "  ")
            else:
                print(f"{elem!r}")


example = {"a": 1, "b": [2, {"c": 3}], "d": {"e": "end"}}
print("  print_json_values({'a':1, 'b':[2,{'c':3}], 'd':{'e':'end'}}):")
print_json_values(example)

# =============================================================================
# 10. COMMON PATTERN - PARSE API RESPONSE THEN ITERATE
# =============================================================================
print("\n--- 10. PARSE THEN ITERATE (API-STYLE) ---")

# Simulated API response string
response_text = '{"items": [{"name": "srv-1", "status": "up"}, {"name": "srv-2", "status": "down"}], "total": 2}'
parsed = json.loads(response_text)

print("  Parsed keys:", list(parsed.keys()))
for entry in parsed["items"]:
    print(f"    {entry['name']}: {entry['status']}")

# =============================================================================
# QUICK REFERENCE
# =============================================================================
print("\n" + "=" * 60)
print("QUICK REFERENCE")
print("=" * 60)
print("""
  json.loads(s)       -> parse string -> dict/list
  json.dumps(obj)     -> dict/list -> string
  json.load(file)     -> read from file -> dict/list
  json.dump(obj, file) -> write dict/list to file

  Iteration:
    dict:  .keys(), .values(), .items()
    list:  for x in lst, or enumerate(lst)
    nested: obj['key']['nested'] or obj['key'][index]

  Options: indent=2 (pretty), sort_keys=True, ensure_ascii=False
  JSON keys are always strings; numbers in JSON become int/float in Python.
""")
print("Done.")
