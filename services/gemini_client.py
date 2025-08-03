import os
import requests
import json

def summarize_data(data, selection):
    prompt = f"""
You are an AI assistant. A user asked for "{selection}" insights for a blockchain wallet.
Summarize the following raw JSON data in simple terms:\n{json.dumps(data)}
Respond in 3-5 lines.
"""
    try:
        res = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
            headers={"Content-Type": "application/json"},
            params={"key": os.getenv("GEMINI_API_KEY")},
            json={"contents": [{"parts": [{"text": prompt}]}]}
        )
        print("Gemini Response:", res.json())
        return res.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        print("Gemini Error:", e)
        return "⚠️ Gemini summarization failed."


def generate_tweet(summary: str) -> str:
    prompt = f"""Generate a concise, tweet-ready message summarizing the following wallet insights. Keep it factual, exciting, and within 280 characters:

{summary}
"""
    res = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        headers={"Content-Type": "application/json"},
        params={"key": os.getenv("GEMINI_API_KEY")},
        json={"contents": [{"parts": [{"text": prompt}]}]},
    )

    try:
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return "Tweet generation failed. Please try again later."