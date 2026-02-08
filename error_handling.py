"""
Python Error Handling Demo - For DevOps Interns
===============================================
Covers: try/except, specific vs generic exceptions, finally, defensive programming,
        cleanup (files, connections, resources).
"""

print("=" * 60)
print("PYTHON ERROR HANDLING - TRY, EXCEPT, FINALLY")
print("=" * 60)

# =============================================================================
# 1. TRY-EXCEPT: PROTECTING SCRIPTS FROM CRASHING
# =============================================================================
print("\n--- 1. TRY-EXCEPT BLOCK ---")
print("Without try/except, one error stops the whole script.")

# Without protection (would crash on error):
# result = 10 / 0   # ZeroDivisionError -> script exits

# With protection: script keeps running
print("\n  Catching an error:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("    Caught ZeroDivisionError; script continues.")
    result = None
print("  Script did not crash. result =", result)

# =============================================================================
# 2. DEFENSIVE PROGRAMMING: CATCH SPECIFIC ERRORS
# =============================================================================
print("\n--- 2. CATCH SPECIFIC ERRORS (Defensive Programming) ---")
print("Catch specific exceptions so you handle only what you expect.")

# --- CORRECT: catch specific exceptions ---
def read_config(path):
    """Handle known failure cases explicitly."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("    FileNotFoundError: config file missing.")
        return None
    except PermissionError:
        print("    PermissionError: cannot read file.")
        return None
    except OSError as e:
        print(f"    OSError (other): {e}")
        return None


# Simulate: no real file read in demo, just show structure
print("  read_config() catches: FileNotFoundError, PermissionError, OSError")

# --- WRONG: bare or too broad Exception ---
# try:
#     with open(path) as f:
#         return f.read()
# except Exception:   # Catches EVERYTHING: KeyboardInterrupt, SystemExit, etc.
#     return None    # Hides bugs and makes debugging hard.

# --- CORRECT: specific first, then broader if needed ---
def parse_port(port_value):
    try:
        return int(port_value)
    except ValueError:
        print("    ValueError: port must be a number.")
        return None
    except TypeError:
        print("    TypeError: port must be a string or number.")
        return None


print("  parse_port() catches ValueError and TypeError separately.")

# =============================================================================
# 3. FINALLY: GUARANTEED EXECUTION
# =============================================================================
print("\n--- 3. FINALLY - GUARANTEED EXECUTION ---")
print("Whether try succeeds or except runs, finally always runs.")

# Example: finally runs on success
print("\n  Case 1: try succeeds -> then finally runs")
try:
    x = 1 + 1
    print("    try: success")
except ValueError:
    print("    except: ran")
finally:
    print("    finally: always runs")

# Example: finally runs when exception is caught
print("\n  Case 2: except catches error -> then finally runs")
try:
    x = 1 / 0
    print("    try: success")
except ZeroDivisionError:
    print("    except: caught ZeroDivisionError")
finally:
    print("    finally: always runs")

# Example: finally runs even when except re-raises
print("\n  Case 3: except re-raises -> finally still runs, then error propagates")
try:
    try:
        raise ValueError("demo")
    except ValueError:
        print("    except: caught, re-raising")
        raise
    finally:
        print("    finally: runs before re-raise")
except ValueError:
    print("  Outer handler caught re-raised error.")

# =============================================================================
# 4. CLEANUP POWER: FILES, CONNECTIONS, RESOURCES
# =============================================================================
print("\n--- 4. CLEANUP - RELEASE RESOURCES (finally) ---")
print("Use finally to close files, DB connections, cloud clients.")

# --- File handle: ensure file is closed ---
print("\n  File handle (ensure close):")
file_handle = None
try:
    # Simulate opening a file (we use a string as stand-in for demo)
    file_handle = "open_file_handle"
    print("    Opened file. Doing work...")
    # raise IOError("disk full")  # Uncomment to simulate error
except IOError as e:
    print(f"    IOError: {e}")
finally:
    if file_handle:
        # In real code: file_handle.close()
        print("    finally: closed file handle")

# --- Pattern: database connection (pseudo-code) ---
print("\n  Database connection (pattern):")
conn = None
try:
    # conn = database.connect(...)
    conn = "connected"
    print("    Connected. Running query...")
except Exception as e:  # pylint: disable=broad-except
    print(f"    Error: {e}")
finally:
    if conn:
        # conn.close()
        print("    finally: closed database connection")

# --- Pattern: cloud client (e.g. Boto3) / external API ---
print("\n  Cloud client / external resource (pattern):")
client = None
try:
    # client = boto3.client('s3')
    client = "boto3_client"
    print("    Using AWS client...")
    # client.download_file(...)
except Exception as e:  # pylint: disable=broad-except
    print(f"    Error: {e}")
finally:
    if client:
        # client.close() or cleanup
        print("    finally: disconnected / released cloud client")

# =============================================================================
# 5. BEST PRACTICES SUMMARY
# =============================================================================
print("\n--- 5. BEST PRACTICES ---")

# Use context manager when possible (no explicit finally needed for files)
print("\n  Prefer 'with' for files (auto-close, no finally needed):")
try:
    # with open("config.yaml") as f:
    #     content = f.read()
    # File closed automatically when block exits
    print("    with open(...) as f: ...  -> file closed automatically")
except FileNotFoundError:
    print("    File not found")

# Else clause: run only when no exception occurred
print("\n  try/except/else: else runs only if no exception:")
try:
    parsed_value = int("42")
except ValueError:
    print("    Invalid number")
else:
    print(f"    Parsed successfully: {parsed_value}")

# =============================================================================
# QUICK REFERENCE
# =============================================================================
print("\n" + "=" * 60)
print("QUICK REFERENCE")
print("=" * 60)
print("""
  try/except     -> Protect script from crashing; catch expected errors.
  Specific first -> except FileNotFoundError, ValueError, ... (not bare Exception).
  finally        -> Always runs: use for cleanup (close file, DB, client).
  with statement -> Prefer "with open(...)" so file is closed automatically.
  else on try     -> Runs only when no exception (optional).

  Cleanup order: try -> except (if error) -> finally -> (re-raise if any)
""")
print("Done.")
