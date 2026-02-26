import time
import requests
import os
import sys

print("=== bot.py module imported ===", flush=True)

BASE_URL = "https://api.kalshi.com/trade-api/v2"

def get_headers():
    api_key = os.environ.get("KALSHI_API_KEY", "")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

def list_markets():
    url = f"{BASE_URL}/markets"
    print("Calling Kalshi /markets at", url, flush=True)
    resp = requests.get(url, headers=get_headers(), timeout=10)
    print("Kalshi status code:", resp.status_code, flush=True)
    resp.raise_for_status()
    return resp.json()

def main():
    print("TOP OF MAIN in Render", flush=True)
    while True:
        print("Loop starting iteration", flush=True)
        try:
            data = list_markets()
            print("Got markets:", len(data.get("markets", [])), flush=True)
        except Exception as e:
            print("Error talking to Kalshi:", repr(e), flush=True)
        time.sleep(10)

if __name__ == "__main__":
    print("__main__ section reached in Render", flush=True)
    main()
