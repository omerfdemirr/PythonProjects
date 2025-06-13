import streamlit as st
import string

st.title("Streamlit ile ilgili örnek çalışmalar")

btn = st.button("Bana tıkla")
if 'i' not in st.session_state:
    st.session_state['i'] = 0

if btn:
    st.session_state['i'] += 1
    st.write("Butona tıkladınız")
    st.write(st.session_state['i'])
else:
    st.write("Henüz tıklamadınız")

st.title("Radio button örneği")
secenek = st.radio("Cinsiyet Seçiniz", ("Erkek", "Kadın"))

if secenek == "Erkek":
    st.write("Erkek seçildi")
else:
    st.write("Kadın seçildi")

st.title("Checkbox button örneği")
onay = st.checkbox("Onay Veriyor musunuz ?")

if onay:
    st.write("Onaylandı")
else:
    st.write("Onaylanmadı")

st.title("Hobileriniz")
hobi1 = st.checkbox("Yüzme")
hobi2 = st.checkbox("Basketbol")
hobi3 = st.checkbox("Sinema")
hobi4 = st.checkbox("Tiyatro")

if hobi1:
    st.write("Yüzme Seçildi")

if hobi2:
    st.write("Basketbol Seçildi")

if hobi3:
    st.write("Sinema Seçildi")

if hobi4:
    st.write("Tiyatro Seçildi")

if not (hobi1 or hobi2 or hobi3 or hobi4):
    st.write("Hiçbir hobi seçilmedi")


#Türkiyenin başkenti nedir

st.title("Türkiyenin başkenti nedir?")

secim = st.radio("Bir seçenek seçin:", ["İstanbul", "Adana", "Ankara", "Malatya"],index=None)

if secim == "İstanbul":
    st.write("İstanbul seçildi")

if secim == "Adana":
    st.write("Adana seçildi")

if secim == "Ankara":
    st.write("Ankara seçildi - Doğru cevap!")

if secim == "Malatya":
    st.write("Malatya seçildi")


st.title("SelectBox Kullanımı")

secim = st.selectbox("Bir Renk seçiniz",("kırmızı","Sarı","Yeşil"),index=None)
if secim:
    st.write(f"Seçtiğiniz Renk: {secim}")

    st.title("Slider örneği")

    yas = st.slider("Yaşınızı seçiniz :",min_value=10,max_value=100,step=1)

    st.write(yas)