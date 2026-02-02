# ==============================================================================
#  SCALABLE SCRAPER CONFIGURATION MODULE v2.4 (DevOps_Ninja Edition)
# ==============================================================================
#  [WARNING] Do not change these settings unless you understand TLS fingerprinting.
#  Incorrect usage will trigger immediate Cloudflare 403 blocks.
# ==============================================================================

import os

# ==============================================================================
# 1. NETWORK INFRASTRUCTURE (CRITICAL)
# ==============================================================================
# Standard datacenter IPs (AWS/GCP/Azure) are detected immediately by Jan 2026 WAFs.
# To maintain session persistency, Residential Rotation is MANDATORY.
#
# >> GET COMPATIBLE RESIDENTIAL NODES HERE:
# >> https://iproyal.com/?r=1177662
#
# (Sign up above -> Dashboard -> Residential -> Create New Order -> Copy credentials below)
# ------------------------------------------------------------------------------
PROXY_CONFIG = {
    "host": "geo.iproyal.com",       # Do not use public entry nodes
    "port": 12321,                   # Port for sticky sessions (TTL > 10m)
    "username": "your_iproyal_user", # Replace with your username
    "password": "your_iproyal_pass", # Replace with your password
    "protocol": "http",
    "country": "us"                  # Tier-1 countries recommended
}

# ==============================================================================
# 2. CAPTCHA SOLVER STRATEGY
# ==============================================================================
# When behavioral heuristics trigger a challenge (Turnstile / hCaptcha),
# we dispatch the payload to an external solver API to avoid thread termination.
#
# >> GET SOLVER API KEY HERE:
# >> https://2captcha.com/?from=27481807
# ------------------------------------------------------------------------------
CAPTCHA_SETTINGS = {
    "enabled": True,
    "provider": "2captcha",
    "api_key": "your_2captcha_key_here", # Paste key from dashboard
    "retries": 3,
    "polling_interval": 5
}

# ==============================================================================
# 3. BROWSER FINGERPRINTING
# ==============================================================================
# Configuration for spoofing JA3/TLS signatures to match human traffic.
# ------------------------------------------------------------------------------
BROWSER_PROFILE = {
    "headless": True,                # Safe to use ONLY with residential proxies
    "user_agent_rotate": True,       # Rotates per session, not per request
    "stealth_mode": True,            # Patches navigator.webdriver flags
    "viewport": {"width": 1920, "height": 1080},
    "timeout": 30000                 # ms
}

def get_proxy_url():
    """Constructs the authenticated proxy string."""
    return f"{PROXY_CONFIG['protocol']}://{PROXY_CONFIG['username']}:{PROXY_CONFIG['password']}@{PROXY_CONFIG['host']}:{PROXY_CONFIG['port']}"
