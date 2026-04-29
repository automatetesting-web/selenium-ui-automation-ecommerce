from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Application configuration
BASE_URL = os.getenv("BASE_URL")

# Test credentials
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

# Safety check (optional but professional)
if not BASE_URL:
    raise ValueError("BASE_URL is not set in environment variables")