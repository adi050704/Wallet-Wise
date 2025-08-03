import requests
import os
from dotenv import load_dotenv

load_dotenv()

def call_bitscrunch(endpoint: str, wallet: str):
    print("Starting call_bitscrunch function")
    if endpoint == 'defi':
        url = f"https://api.unleashnfts.com/api/v2/wallet/balance/defi?address={wallet}&blockchain=ethereum&time_range=all&offset=0&limit=30"
    elif endpoint == 'nft':
        url = f"https://api.unleashnfts.com/api/v2/wallet/balance/nft?wallet={wallet}&blockchain=ethereum&time_range=all&offset=0&limit=30"
    elif endpoint == 'token':
        url = f"https://api.unleashnfts.com/api/v2/wallet/balance/token?address={wallet}&blockchain=ethereum&time_range=all&offset=0&limit=30"
    elif endpoint == 'label':
        url = f"https://api.unleashnfts.com/api/v2/wallet/label?address={wallet}&blockchain=ethereum&offset=0&limit=30"
    elif endpoint == 'score':
        url = f"https://api.unleashnfts.com/api/v2/wallet/score?wallet_address={wallet}&time_range=all&offset=0&limit=30"
    elif endpoint == 'metrics':
        url = f"https://api.unleashnfts.com/api/v2/wallet/metrics?blockchain=ethereum&wallet={wallet}&time_range=all&offset=0&limit=30"
    else:
        raise ValueError(f"Unsupported endpoint: {endpoint}")
    print("Constructed URL:", url)
    headers = {
        "accept": "application/json",
        "x-api-key": os.getenv("BITSCRUNCH_API_KEY")
    }
    try:
        print("Sending request to URL")
        res = requests.get(url, headers=headers)
        print("Response Status Code:", res.status_code)
        print("Response JSON:", res.json())
        return res.json()
    except Exception as e:
        print("Error occurred during request:", e)
        return None
    print("Finished call_bitscrunch function")
