import streamlit as st
import  requests as rq

response = rq.get("https://dog.ceo/api/breeds/image/random")
veri=response.json()

resim=veri.get("message")
st.image(resim)
st.balloons()
st.button("Yenile")