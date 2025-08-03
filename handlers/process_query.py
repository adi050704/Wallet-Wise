from services.bitscrunch_api import call_bitscrunch
from services.gemini_client import summarize_data, generate_tweet

endpoint_map = {
    "DeFi Portfolio": "defi",
    "NFT Portfolio": "nft",
    "ERC20 Portfolio": "token",
    "Wallet Score": "score",
    "Wallet Label": "label",
    "Wallet Metrics": "metrics"
}

async def fetch_and_summarize(wallet: str, selection: str) -> str:
    endpoint = endpoint_map.get(selection)
    if not endpoint:
        return "Unknown option selected."

    data = call_bitscrunch(endpoint, wallet)
    print("Data:",data)
    if not data:
        return "No data found for this wallet."

    summary = summarize_data(data, selection)
    print("Summary:",summary)
    tweet = generate_tweet(summary)
    return summary + "\n\n📢 Suggested Tweet:\n" + tweet
