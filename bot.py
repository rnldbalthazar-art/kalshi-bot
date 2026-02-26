import time
import requests
import os

print("=== bot.py module imported ===")  # NEW

BASE_URL = "https://api.kalshi.com/trade-api/v2"

def get_headers():
    api_key = os.environ.get("KALSHI_API_KEY", "")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

def list_markets():
    url = f"{BASE_URL}/markets"
    resp = requests.get(url, headers=get_headers(), timeout=10)
    resp.raise_for_status()
    return resp.json()

def main():
    print("TOP OF MAIN in Render")  # test log
    while True:
        print("Loop starting iteration")  # test log
        try:
            data = list_markets()
            print("Got markets:", len(data.get("markets", [])))
        except Exception as e:
            print("Error talking to Kalshi:", repr(e))
        time.sleep(10)  # shorter for testing

if __name__ == "__main__":
    print("__main__ section reached in Render")  # test log
    main()
