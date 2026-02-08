"""
Python Functions Demo - For DevOps Interns
==========================================
Covers: defining functions, positional/keyword args, default values,
        *args, **kwargs, return values
"""

print("=" * 60)
print("PYTHON FUNCTIONS - ARGUMENTS AND PARAMETERS")
print("=" * 60)

# =============================================================================
# 1. BASIC FUNCTION - NO ARGUMENTS
# =============================================================================
print("\n--- 1. BASIC FUNCTION (no arguments) ---")


def greet():
    """Function with no parameters."""
    print("  Hello from greet()!")


greet()

# =============================================================================
# 2. POSITIONAL ARGUMENTS
# =============================================================================
print("\n--- 2. POSITIONAL ARGUMENTS ---")


def deploy(app_name, environment):
    """Arguments passed by position: first value -> app_name, second -> environment."""
    print(f"  Deploying {app_name} to {environment}")


deploy("api-service", "production")
deploy("staging", "web-app")  # Order matters! Easy to mix up.

# =============================================================================
# 3. KEYWORD ARGUMENTS (named arguments)
# =============================================================================
print("\n--- 3. KEYWORD ARGUMENTS ---")


def start_server(host, port):
    """Same function, but call with names = no confusion."""
    print(f"  Starting server at {host}:{port}")


# Positional
start_server("0.0.0.0", 8080)

# Keyword (order doesn't matter)
start_server(port=3000, host="localhost")
start_server(host="127.0.0.1", port=5000)

# Mix: positional first, then keyword (keyword cannot come before positional)
start_server("0.0.0.0", port=9000)

# =============================================================================
# 4. DEFAULT ARGUMENT VALUES
# =============================================================================
print("\n--- 4. DEFAULT VALUES ---")


def connect(host="localhost", port=5432, ssl=False):
    """Parameters with defaults; caller can omit them."""
    print(f"  Connect: {host}:{port}, ssl={ssl}")


connect()                          # All defaults
connect("db.example.com")          # Just host; port and ssl default
connect(port=3306)                 # Just port; host and ssl default
connect("db.example.com", 5433, True)  # Override all

# =============================================================================
# 5. RETURN VALUES
# =============================================================================
print("\n--- 5. RETURN VALUES ---")


def check_disk_usage(path="/"):
    """Function returns a value; caller uses it."""
    # Simulated usage percent
    return 75


def get_status_message(code):
    """Return different values based on logic."""
    if code == 200:
        return "OK"
    elif code == 404:
        return "Not Found"
    else:
        return "Error"


usage = check_disk_usage()
print(f"  Disk usage: {usage}%")

msg = get_status_message(404)
print(f"  Status 404 -> {msg}")

# Return multiple values (as a tuple)
def get_server_info():
    return "web-01", 8080, True  # host, port, healthy


host, port, healthy = get_server_info()
print(f"  Unpacked return: host={host}, port={port}, healthy={healthy}")

# =============================================================================
# 6. *args - VARIABLE NUMBER OF POSITIONAL ARGUMENTS
# =============================================================================
print("\n--- 6. *args (variable positional args) ---")


def add_ports(*ports):
    """*args collects extra positional args into a tuple."""
    print(f"  ports (tuple): {ports}")
    return sum(ports)


total = add_ports(80, 443, 8080)
print(f"  Sum of ports: {total}")

add_ports(22)           # One value
add_ports(80, 443)      # Two values


def log_levels(*levels):
    """Common use: pass a list of items."""
    for level in levels:
        print(f"    - {level}")


print("  Log levels:")
log_levels("INFO", "WARNING", "ERROR")

# =============================================================================
# 7. **kwargs - VARIABLE NUMBER OF KEYWORD ARGUMENTS
# =============================================================================
print("\n--- 7. **kwargs (variable keyword args) ---")


def build_config(**options):
    """**kwargs collects extra keyword args into a dict."""
    print(f"  options (dict): {options}")
    return options


cfg = build_config(host="0.0.0.0", port=8080, debug=True)
print(f"  Returned config: {cfg}")

# Typical use: pass through or merge config
build_config(env="production", region="us-east-1")


def merge_env(**env_vars):
    """Merge keyword args as environment variables."""
    base = {"PATH": "/usr/bin", "HOME": "/root"}
    base.update(env_vars)
    return base


merged = merge_env(API_KEY="secret", LOG_LEVEL="DEBUG")
print(f"  Merged env: {merged}")

# =============================================================================
# 8. COMBINING: positional, *args, keyword, **kwargs
# =============================================================================
print("\n--- 8. COMBINING PARAMETERS ---")


def run_command(cmd, *args, verbose=False, **kwargs):
    """
    Order: positional, *args, keyword-only (optional), **kwargs
    """
    print(f"  cmd: {cmd}, args: {args}, verbose: {verbose}, kwargs: {kwargs}")


run_command("docker", "run", "-d", "nginx")
run_command("kubectl", "get", "pods", verbose=True, namespace="default")
run_command("echo", "hello", env="prod")

# =============================================================================
# 9. PASSING LIST/DICT AS ARGUMENTS
# =============================================================================
print("\n--- 9. PASSING COLLECTIONS ---")


def restart_servers(servers):
    """Pass a list (or any iterable) as one argument."""
    for s in servers:
        print(f"    Restarting {s}")


restart_servers(["web-01", "web-02", "db-01"])


def apply_config(config_dict):
    """Pass a dict as one argument."""
    for k, v in config_dict.items():
        print(f"    {k} = {v}")


apply_config({"timeout": 30, "retries": 3})

# Unpacking into arguments
ports_list = [80, 443, 8080]
print("  Unpack list with *:")
print(f"    add_ports(*ports_list) -> {add_ports(*ports_list)}")

options_dict = {"host": "api.example.com", "port": 443}
print("  Unpack dict with **:")
start_server(**options_dict)

# =============================================================================
# QUICK REFERENCE
# =============================================================================
print("\n" + "=" * 60)
print("QUICK REFERENCE")
print("=" * 60)
print("""
  def name():           -> no arguments
  def name(a, b):       -> positional (order matters)
  def name(a=1, b=2):   -> default values
  name(x=1, y=2)       -> keyword arguments (order free)
  def name(*args):      -> extra positionals -> tuple
  def name(**kwargs):   -> extra keywords -> dict
  return x              -> single value
  return a, b           -> multiple values (tuple)
  func(*list)           -> unpack list to positionals
  func(**dict)          -> unpack dict to keywords
""")
print("Done.")
