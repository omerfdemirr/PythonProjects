import streamlit as st

st.title("Kayıt Formu")

with st.form("Kayıt_formu"):
    ad = st.text_input("Ad Soyad")
    email = st.text_input("E Posta")
    sifre = st.text_input("Şifre",type="password")
    sifre_tekrar= st.text_input("Şifre (Tekrar)",type="password")
    kayit_button = st.form_submit_button("Kayıt Ol")

    if kayit_button:
       if not ad or not email or not sifre or not sifre_tekrar:
           st.warning("Lütfen Tüm Alanları Doldurunuz.")
       elif sifre!=sifre_tekrar:
           st.error("Şifreler Uyuşmuyor")
       else:
           st.balloons()
           st.success(f"Hoş geldiniz, {ad} Kayıt işleminiz tamamlandı")