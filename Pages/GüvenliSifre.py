import string
import streamlit as st

kh = string.ascii_lowercase
bh = string.ascii_uppercase
rk = string.digits
sy = string.punctuation

sifre = st.text_input("Şifre Giriniz")

kucukSay = any(harf in sifre for harf in kh)
buyukSay = any(harf in sifre for harf in bh)
rakamSay = any(harf in sifre for harf in rk)
sembolSay = any(harf in sifre for harf in sy)
uzunluk = len(sifre) > 8

if kucukSay and buyukSay and rakamSay and sembolSay and uzunluk:
    st.write("Şifre Güvenlidir")
else:
    st.write("Şifre Güvenli değildir")