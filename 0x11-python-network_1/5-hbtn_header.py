#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""


import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
