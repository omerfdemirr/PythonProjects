import streamlit as st
import requests as rq

st.title("Hava Durumu")
sehir = st.text_input("Şehir giriniz")
btn = st.button("Hava Durumu getir")

if btn:
    if sehir:
        api_url = f"http://api.weatherapi.com/v1/current.json?key=a369315e7050407bbc3160831252103&q={sehir}&aqi=no"
        response = rq.get(api_url)

        if response.status_code == 200:
            data = response.json()
            sicaklik_celsius = data['current']['temp_c']
            durum = data['current']['condition']['text']
            ikon_url = "https:" + data['current']['condition']['icon']

            st.write(f"**Hava durumu: {sehir}**")
            st.write(f"**Sıcaklık:** {sicaklik_celsius} °C")
            st.write(f"**Durum:** {durum}")
            st.image(ikon_url, caption="Hava Durumu İkonu")

        else:
            st.error("Hava durumu bilgisi alınamadı. Lütfen geçerli bir şehir girin.")
    else:
        st.warning("Lütfen bir şehir giriniz.")