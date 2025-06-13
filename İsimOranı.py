import streamlit as st
import requests as rq

st.title("İsmin Ülkelerce Kullanım Oranı")

isim = st.text_input("İsminizi Giriniz")

btn = st.button("Sonuçlar")

if btn:
    url = f"https://api.nationalize.io/?name={isim}"
    r = rq.get(url)
    veri = r.json().get("country", [])

    if veri:
        for ulke in veri:
            st.write(f"{ulke.get('country_id')} - %{ulke.get('probability') * 100:.2f}")
    else:
        st.write("Bu isim için veri bulunamadı.")