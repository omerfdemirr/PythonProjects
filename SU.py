import streamlit as st
import time
import random
import requests

# Sayfa ayarları
st.set_page_config(page_title="Sevgiline Özel Barışma Uygulaması ❤️", page_icon="🐶", layout="centered")

# Başlık
st.markdown('<div class="title">Sevgiline Özel Barışma Mesajı 💖</div>', unsafe_allow_html=True)

# Kullanıcıdan sevgilinin adını alma
isim = st.text_input("Sevgilinin Adı", max_chars=30)

# Kullanıcıdan özel fotoğraf veya video yüklemesini isteme
uploaded_video = st.file_uploader("Sevgiline özel video yükle 🎥", type=["mp4", "avi", "mov"])
uploaded_photo = st.file_uploader("Sevgiline özel fotoğraf yükle 💑", type=["jpg", "jpeg", "png"])

# Sevgi mesajları
sevgi_mesajlari = [
    "Seni her şeyden çok seviyorum, hayatımın anlamı sensin! ❤️",
    "Kalbim yalnızca senin için atıyor, lütfen beni affet. 💕",
    "Seninle yaşamak, dünyadaki en güzel mucize... Barışalım mı? 🌹",
    "Hayat sensiz eksik, barışalım ve yeni bir sayfa açalım! 😊",
    "Senin gülüşün, benim en büyük mutluluğum. Affet beni lütfen! 💖",
]

# API'den rastgele komik köpek fotoğrafı çekme
def get_funny_dog():
    response = requests.get("https://random.dog/woof.json")
    if response.status_code == 200:
        return response.json()["url"]
    return "https://www.rd.com/wp-content/uploads/2021/01/GettyImages-1175550351.jpg"  # Yedek komik köpek fotoğrafı

funny_dog_url = get_funny_dog()

# Kullanıcının yüklediği video veya fotoğrafı gösterme
if uploaded_video:
    st.video(uploaded_video)

if uploaded_photo:
    st.image(uploaded_photo, caption="Sevgiline Özel Fotoğraf 💞", use_container_width=True)

# Barış butonu ve mesaj gösterme
if isim:
    if st.button("Barışalım!", key="baris_buton", help="Bu butona tıkladığında büyülü bir mesaj gelecek!"):
        st.balloons()
        with st.spinner("Mesaj hazırlanıyor..."):
            time.sleep(1.5)
        mesaj = random.choice(sevgi_mesajlari)
        st.markdown(f'<div class="message-box">{mesaj}</div>', unsafe_allow_html=True)
        st.image(funny_dog_url, caption="Bu komik köpek seni affetmeye hazır mı? 🐶😂", use_container_width=True)
else:
    st.info("Lütfen sevgilinin adını gir ve kalbini aç! 💌")