import streamlit as st
import requests as rq

response = rq.get("https://www.amiiboapi.com/api/amiibo/")

if response.status_code == 200:
    veri = response.json().get("amiibo", [])
else:
    st.error("Veri alınamadı!")

karakter = {}

for k in veri:
    karakter[k.get("name")] = k.get("image")

secilen = st.selectbox("Karakter seç", karakter.keys())

with st.expander("Karakter görseli"):
    if secilen in karakter:
        st.image(karakter[secilen])
    else:
        st.warning("Görsel bulunamadı!")


    