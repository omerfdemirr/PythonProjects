import streamlit as st
import requests as rq



st.title("Kur Çevirici")

response=rq.get("https://open.er-api.com/v6/latest/TRY")
veri=response.json()
veri=veri.get()