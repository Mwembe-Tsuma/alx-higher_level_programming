#!/usr/bin/python3
"""
Python script that takes your GitHub credentials username and password
and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == "__main__":
    username, access_token = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    page = requests.get(url, auth=(username, access_token))

    if page.status_code == 200:
        user_data = page.json()
        user_id = user_data.get("id")
        print(f"Your GitHub user ID: {user_id}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
