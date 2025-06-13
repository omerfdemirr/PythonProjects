import requests
import streamlit as st
import  requests as rq

r=requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
veri=r.json()
soru=veri.get("setup")
cevap=veri.get("delivery")

st.title(soru)

with st.expander("Cevabı.."):
    st.write(cevap)

    st.button("Yeni Soru")