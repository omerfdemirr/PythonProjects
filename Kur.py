import streamlit as st
import requests as rq

st.set_page_config(page_title="Döviz Çevirici")
st.title("TL Çevirici")

para_birimleri = ["USD", "EUR"]
secim = st.selectbox("Para Birimini Seçiniz", para_birimleri)

miktar = st.number_input(f"{secim} Miktarını Giriniz:", min_value=0.0)

kur = None
try:
    response = rq.get(f"https://open.er-api.com/v6/latest/{secim}")
    response.raise_for_status()
    data = response.json()
    kur = data["rates"]["TRY"]
except:
    st.error(f"{secim}/TRY kuru alınamadı !!")

if kur and miktar > 0:
    tl_karsiligi = miktar * kur
    st.balloons()
    st.success(f"{miktar:.2f} {secim} ≈ ₺{tl_karsiligi:,.2f}")
