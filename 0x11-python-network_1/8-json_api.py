#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user
"""

import requests
from sys import argv

letter = sys.argv[1] if len(sys.argv) > 1 else ""

url = "http://0.0.0.0:5000/search_user"
params = {"q": letter}

page = requests.post(url, params=params)

try:
    data = page.json()
    if data:
        print(f"[{data.get('id')}] {data.get('name')}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
except Exception as e:
    print(f"An error occurred: {e}")
