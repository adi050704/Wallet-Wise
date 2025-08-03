# 🧠 WalletWise - AI Powered Wallet Analyzer

**WalletWise** is a smart Telegram bot that helps users analyze blockchain wallet health and portfolio insights in real time. Powered by the **bitsCrunch APIs** and **Gemini 2.0 Flash**, it summarizes DeFi, NFT, and ERC20 activity and generates shareable tweet summaries - all through a conversational interface.

---

Live Link: [WalletWise Bot](https://t.me/walletwise25_bot)

---

Demo Video: [WalletWise Demo](https://youtu.be/VfdlxrKklHQ)

---

## 🚀 Features

- ✅ Ask users for their wallet address
- 📊 Provide interactive options like:
  - DeFi Portfolio
  - NFT Portfolio
  - ERC20 Portfolio
  - Wallet Score
  - Wallet Metrics
- 🔎 Fetches real-time wallet data from **bitsCrunch APIs**
- 💡 Uses **Gemini 2.0 Flash** to summarize wallet activity
- 🐦 Instantly generates a **tweet-ready summary**
- 🧠 Stateless UX using Telegram’s built-in reply keyboards

---

## 🧩 Tech Stack

- Python
- `python-telegram-bot`
- `requests`
- Google Gemini 2.0 Flash (via PaLM API)
- bitsCrunch APIs

---

## 🧠 How it Works

1. **User starts the bot** with `/start`
2. **Prompted for wallet address**
3. **Bot displays analysis options** (e.g., DeFi Portfolio)
4. On selection:
   - Wallet data is fetched from the respective bitsCrunch API
   - Gemini 2.0 Flash generates a concise summary
   - A tweet version is also generated and sent

---

## Screenshot

<img width="1065" height="717" alt="Screenshot 2025-08-03 at 8 59 30 PM" src="https://github.com/user-attachments/assets/30f51d8f-08b9-4bd9-83a8-73cb7c550063" />
