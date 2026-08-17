"""
Check an Optional pip Package
Created by Ahmad Akhtar

Beginner-friendly Python practice file.
Run: python "check_pip_package.py"
"""

try:
    import requests
    print("requests is installed. Version:", requests.__version__)
except ImportError:
    print("requests is not installed. Try: pip install requests")

