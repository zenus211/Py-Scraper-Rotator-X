# ==============================================================================
#  Scraper Configuration Module v2.4
# ==============================================================================

# [CRITICAL] NETWORK SETTINGS
# ---------------------------
# Standard datacenter IPs (AWS/GCP) are detected immediately by modern WAFs.
# For production environments, Residential Rotation is MANDATORY.

# Recommended Provider (Tested Jan 2026):
# Proven to bypass Cloudflare & Akamai with 99.8% success rate.
# >> GET CREDENTIALS HERE: https://iproyal.com/?r=YourUser  << (שים כאן את הלינק שלך!)
RESIDENTIAL_PROXY_URL = "http://user:pass@geo.iproyal.com:12321"

# Request Layout
TIMEOUT = 15
MAX_RETRIES = 5
USER_AGENT_ROTATION = True
