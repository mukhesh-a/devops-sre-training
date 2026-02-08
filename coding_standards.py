"""
Coding Standards - Correct vs Wrong Usage
=========================================
For DevOps / Python projects.

The Standardized Mindset:
    "Code is read more often than it is written."
"""

# =============================================================================
# 1. NAMING CONVENTIONS
# =============================================================================
# Rule: snake_case for functions and variables, PascalCase for classes.

# --- CORRECT: snake_case for functions and variables ---
def get_server_status():
    """Fetch current server status."""
    max_retry_count = 3
    connection_timeout = 30
    return "ok"


api_base_url = "https://api.example.com"
disk_usage_percent = 85

# --- WRONG: camelCase or other styles for functions/variables ---
# def getServerStatus():      # Avoid camelCase for functions
#     maxRetryCount = 3       # Avoid camelCase for variables
#     connectionTimeout = 30
# APIBaseUrl = "..."          # Avoid PascalCase for variables (that's for classes)

# --- CORRECT: PascalCase for classes ---
class DeploymentConfig:
    """Holds deployment configuration."""

    def __init__(self, environment, region):
        self.environment = environment
        self.region = region


class HealthChecker:
    """Checks service health."""

    def run_check(self):
        return True


# --- WRONG: snake_case or lowercase for class names ---
# class deployment_config:    # Wrong: classes should be PascalCase
#     pass
# class healthchecker:        # Wrong: not PascalCase

# =============================================================================
# 2. FORMATTING - INDENTATION
# =============================================================================
# Rule: 4 spaces per indentation level. Never use tabs.

# --- CORRECT: 4 spaces per level ---
def process_servers(servers):
    results = []
    for server in servers:
        if server.is_healthy():
            results.append(server.name)
        else:
            results.append(None)
    return results


# --- WRONG: tabs or 2 spaces (unless project standard is 2) ---
# def process_servers(servers):
# →   results = []              # Wrong: tab character
# →   for server in servers:
# → →     if server.is_healthy():  # Wrong: 2 spaces inconsistent with 4-space standard
#     return results

# =============================================================================
# 3. IMPORTS - GROUPING AND ORDER
# =============================================================================
# Rule: Group in order — (1) standard library, (2) third-party, (3) local.
#       One import per line for multiple modules; blank line between groups.

# --- CORRECT: grouped and ordered ---
import os
import sys
from pathlib import Path

import requests
import yaml

from config import load_config
from utils.helpers import retry


# --- WRONG: mixed order, no grouping ---
# import requests
# from config import load_config
# import os
# import yaml
# from pathlib import Path
# import sys

# --- CORRECT: one per line when importing multiple names ---
from collections import defaultdict, OrderedDict

# --- WRONG: multiple modules on one line (hard to read/grep) ---
# import os, sys, json  # Avoid

# =============================================================================
# 4. READABILITY (Mindset: "Code is read more often than written")
# =============================================================================

# --- CORRECT: clear names and simple logic ---
def check_disk_space(path, warning_threshold_percent=85):
    """Return True if disk usage is below warning threshold."""
    usage = get_disk_usage_percent(path)
    return usage < warning_threshold_percent


# --- WRONG: cryptic names, no docstring ---
# def chk(p, t=85):    # What is chk? What is p?
#     u = get_disk_usage_percent(p)
#     return u < t

# --- CORRECT: meaningful variable names in loops ---
for server in servers:
    if server.port == 443:
        restart(server)


# --- WRONG: single-letter or vague names when meaning isn't obvious ---
# for s in servers:
#     if s.port == 443:
#         restart(s)   # 's' is acceptable in short loops; 'server' is clearer

# =============================================================================
# QUICK REFERENCE
# =============================================================================
"""
  Naming:
    ✓ snake_case   for functions, variables, modules
    ✓ PascalCase   for classes
    ✗ camelCase    for functions/variables in Python
    ✗ PascalCase   for variables (only for classes)

  Formatting:
    ✓ 4 spaces per indentation level
    ✗ Tabs
    ✗ Mixing 2 and 4 spaces

  Imports (order):
    1. Standard library  (os, sys, pathlib, etc.)
    2. Third-party       (requests, yaml, etc.)
    3. Local             (config, utils.helpers, etc.)
    ✓ Blank line between groups
    ✓ One import per line for different modules
"""
