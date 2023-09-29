import requests
import sys

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
