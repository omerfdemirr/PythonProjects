import streamlit as st
import requests

# Sayfa başlığı
st.title("💰 Canlı Kripto Para Fiyatları")

# Kullanıcıdan veri alma
st.write("Hangi para birimiyle görmek istersiniz?")
vs_currency = st.selectbox("Para Birimi Seçin:", ["usd", "eur", "try"])

# Buton
if st.button("🔎 Fiyatları Getir"):
    # API isteği
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={vs_currency}&order=market_cap_desc&per_page=10&page=1&sparkline=false"
    response = requests.get(url)
    data = response.json()

    # Kripto paraları ekrana yazdır
    if data:
        st.subheader(f"📈 {vs_currency.upper()} Piyasasında En Büyük 10 Kripto Para")
        for coin in data:
            st.image(coin["image"], width=50)  # Kripto para logosunu ekle
            st.write(f"**{coin['name']} ({coin['symbol'].upper()})** → 💵 {coin['current_price']} {vs_currency.upper()}")
    else:
        st.error("Veri alınamadı, lütfen tekrar deneyin.")

        