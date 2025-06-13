import streamlit as st
import requests

st.set_page_config(page_title="Kripto Para Fiyatları", page_icon="📈")

st.title("📈 Kripto Para Fiyat Takibi")

# Kullanıcının seçeceği kripto paralar
available_coins = {
    "Bitcoin (BTC)": "btcusd",
    "Ethereum (ETH)": "ethusd",
    "Solana (SOL)": "solusd",
    "Dogecoin (DOGE)": "dogeusd",
    "Ripple (XRP)": "xrpusd"
}

selected_coin = st.selectbox("Bir kripto para seçin", list(available_coins.keys()))
symbol = available_coins[selected_coin]

# Gemini API'den kripto para fiyatını al
crypto_url = f"https://api.gemini.com/v1/pubticker/{symbol}"
crypto_response = requests.get(crypto_url)

if crypto_response.status_code == 200:
    crypto_data = crypto_response.json()
    crypto_usd_price = float(crypto_data["last"])
    st.metric(f"{selected_coin} (USD)", f"${crypto_usd_price:,.4f}")
else:
    st.error("Kripto para verisi alınamadı.")

# USD/TRY kuru
usd_response = requests.get("https://open.er-api.com/v6/latest/USD")
if usd_response.status_code == 200:
    usd_data = usd_response.json()
    usd_try = float(usd_data["rates"]["TRY"])
    crypto_try_price = crypto_usd_price * usd_try
    st.metric(f"{selected_coin} (TRY)", f"₺{crypto_try_price:,.2f}")
else:
    st.error("USD/TRY kuru alınamadı.")
