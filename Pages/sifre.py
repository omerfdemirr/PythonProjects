import random
import string
import streamlit as st

st.title("Şifre Oluşturucu")

# Karakter setlerini belirle
kh = string.ascii_lowercase
bh = string.ascii_uppercase
rk = string.digits
sb = string.punctuation

# Şifre oluşturma fonksiyonu
def generate_password():
    khsec = random.choices(kh, k=2)
    bhsec = random.choices(bh, k=2)
    rksec = random.choices(rk, k=2)
    sbsec = random.choices(sb, k=2)

    sifre = khsec + bhsec + rksec + sbsec
    random.shuffle(sifre)
    return ''.join(sifre)

# Buton ile şifre oluşturma
if st.button("Şifre Oluştur"):
    st.write("Oluşturulan Şifre:", generate_password())