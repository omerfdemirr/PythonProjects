import streamlit as st

st.title("Form Application")

with st.form(key="my_form"):
    isim = st.text_input("İsim Giriniz")
    cinsiyet = st.radio("Cinsiyet",("Erkek","Kadın"),index=None)
    onay = st.checkbox("Sözleşmeyi Kabul Ettiniz")
    renk = st.selectbox("Renk Seçiniz",("Kırmızı","Sarı","Mavi"))
    yas = st.slider("Yaşınız",min_value=18,max_value=60,step=1)
    submit_btn=st.form_submit_button(label="Gönder")

    if submit_btn:
        if onay:
            st.write(f"Merhaba,{isim}")
            st.write(f"Cinsiyetiniz{cinsiyet}")
            st.write(f"Renk Seçimi:{renk}")
            st.write(f"Yaşınız:{yas}")
        else:
            st.write("Onay Vermelisiniz...")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("Sütun 1")
                st.text_area(label="Adres")

            with col2:
                st.write("Sütun 2")

            with col3:
                st.write("Sütun 3")
