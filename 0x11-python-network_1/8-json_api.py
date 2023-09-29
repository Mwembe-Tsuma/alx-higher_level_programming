#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user
"""

import requests
from sys import argv

if __name__ == "__main__":
    data = {"q": argv[1] if len(argv) > 1 else ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
