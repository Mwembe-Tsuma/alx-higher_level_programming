#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    try:
        page = requests.get(url)
        page.raise_for_status()

        commits = page.json()
        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
