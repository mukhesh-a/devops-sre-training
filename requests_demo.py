"""
Python Requests Package Demo - For DevOps Interns
=================================================
Simple HTTP calls: GET, status codes, response body.
Uses public endpoints that do NOT require authentication (demo only).

Install: pip install requests   (or: python -m pip install requests)
"""

import requests

print("=" * 60)
print("REQUESTS PACKAGE - API PING & STATUS CODES (No Auth)")
print("=" * 60)

# Public demo endpoints (no API key or token needed)
# httpbin.org - echo service for testing
# httpstat.us - returns specific HTTP status codes

# =============================================================================
# 1. SIMPLE GET REQUEST
# =============================================================================
print("\n--- 1. SIMPLE GET REQUEST ---")

demo_url = "https://httpbin.org/get"
print(f"  GET {demo_url}")

response = requests.get(demo_url, timeout=5)

# Status code (e.g. 200, 404, 500)
print(f"  response.status_code = {response.status_code}")

# Boolean: True if status is 2xx
print(f"  response.ok = {response.ok}")

# =============================================================================
# 2. USING STATUS CODE FOR DECISIONS (API PING)
# =============================================================================
print("\n--- 2. API PING - CHECK STATUS CODE ---")


def ping_url(target_url):
    """Ping a URL and return status code; no auth."""
    try:
        resp = requests.get(target_url, timeout=5)
        return resp.status_code
    except requests.RequestException as e:
        print(f"  Request failed: {e}")
        return None


# Ping a public endpoint
status = ping_url("https://httpbin.org/get")
print(f"  ping_url('https://httpbin.org/get') -> status_code = {status}")

if status == 200:
    print("  -> API is UP (200 OK)")
elif status:
    print(f"  -> API returned {status}")
else:
    print("  -> Request failed (timeout/connection error)")

# =============================================================================
# 3. RESPONSE BODY - .text AND .json()
# =============================================================================
print("\n--- 3. RESPONSE BODY ---")

response2 = requests.get("https://httpbin.org/get", timeout=5)
print(f"  Status: {response2.status_code}")

# Raw text
print(f"  resp.text (first 80 chars): {response2.text[:80]}...")

# Parsed JSON (for JSON APIs)
data = response2.json()
print(f"  resp.json() -> type: {type(data).__name__}")
print(f"  data['url'] = {data.get('url')}")

# =============================================================================
# 4. DIFFERENT STATUS CODES (DEMO)
# =============================================================================
print("\n--- 4. HANDLING DIFFERENT STATUS CODES ---")

# httpstat.us returns the status you ask for (good for demo)
test_cases = [
    ("https://httpstat.us/200", 200),
    ("https://httpstat.us/404", 404),
    ("https://httpstat.us/500", 500),
]

for test_url, expected in test_cases:
    res = requests.get(test_url, timeout=5)
    code = res.status_code
    ok = "OK" if res.ok else "not OK"
    print(f"  {test_url} -> {code} (response.ok = {ok})")

# =============================================================================
# 5. COMMON PATTERN: PING AND BRANCH ON STATUS
# =============================================================================
print("\n--- 5. TYPICAL PING PATTERN ---")


def check_api_health(health_url):
    """
    Ping URL; no auth. Return True if 2xx, else False.
    """
    try:
        resp = requests.get(health_url, timeout=5)
        if resp.ok:
            print(f"  Health OK: {health_url} -> {resp.status_code}")
            return True
        print(f"  Health BAD: {health_url} -> {resp.status_code}")
        return False
    except requests.RequestException as e:
        print(f"  Health FAIL: {health_url} -> {e}")
        return False


check_api_health("https://httpbin.org/status/200")
check_api_health("https://httpbin.org/status/503")

# =============================================================================
# QUICK REFERENCE
# =============================================================================
print("\n" + "=" * 60)
print("QUICK REFERENCE (no auth demos)")
print("=" * 60)
print("""
  requests.get(url, timeout=5)  -> GET request
  response.status_code          -> 200, 404, 500, etc.
  response.ok                   -> True if 2xx
  response.text                 -> body as string
  response.json()               -> body as dict (for JSON APIs)

  Try/except requests.RequestException for timeouts and connection errors.
  Use public URLs (e.g. httpbin.org, httpstat.us) for demos without tokens.
""")
print("Done.")
