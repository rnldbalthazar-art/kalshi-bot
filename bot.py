import time
import requests
import os

BASE_URL = "https://api.kalshi.com/trade-api/v2"

def get_headers():
    api_key = os.environ.get("KALSHI_API_KEY", "")
    if not api_key:
        print("ERROR: KALSHI_API_KEY is not set in environment")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

def list_markets():
    url = f"{BASE_URL}/markets"
    print("Calling Kalshi /markets at", url)
    resp = requests.get(url, headers=get_headers(), timeout=10)
    print("Kalshi status code:", resp.status_code)
    resp.raise_for_status()
    return resp.json()

def main():
    print("Render Kalshi bot starting...")
    while True:
        try:
            data = list_markets()
            print("Got markets:", len(data.get("markets", [])))
        except Exception as e:
            print("Error talking to Kalshi:", repr(e))
        time.sleep(60)

if __name__ == "__main__":
    main()
