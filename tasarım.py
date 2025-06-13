import streamlit as st

# Sayfa başlığı ve açıklama
st.set_page_config(page_title="Streamlit Sayfa Tasarımı", layout="wide")
st.title("Streamlit ile Şık Sayfa Tasarımı")
st.write("Bu örnek, Streamlit ile bir sayfanın nasıl düzenlenebileceğini gösterir.")

# Yan menü (Sidebar)
st.sidebar.title("Yan Menü")
sayfa_secimi = st.sidebar.radio("Sayfa Seçimi", ("Ana Sayfa", "Ayarlar", "İletişim"))
st.sidebar.write("Bu menüden sayfa seçebilirsiniz")
kamera_secimi = st.sidebar.camera_input("Kamera alanı")
dosya_yukleme = st.sidebar.file_uploader("Dosya yükle", type=["jpg", "png", "csv"])
progress_bar = st.sidebar.progress(50)  # %50 ilerleme çubuğu

# Ana sayfa düzeni
if sayfa_secimi == "Ana Sayfa":
    st.header("Ana Sayfa")

    # Sütunlar ile içerik düzenleme
    col1, col2 = st.columns(2)  # Sayfayı 2 sütuna böler
    with col1:
        st.subheader("Grafik 1")
        st.line_chart({"Veri 1": [1, 2, 3, 4], "Veri 2": [5, 4, 3, 2]})

    with col2:
        st.subheader("Grafik 2")
        st.bar_chart({"Kategori A": [10, 20, 30], "Kategori B": [30, 20, 10]})

    # Ek bileşenler
    st.subheader("Kullanıcı Girdileri")
    isim = st.text_input("Adınızı girin")
    secim = st.selectbox("Seçim yapın", ["Seçenek 1", "Seçenek 2", "Seçenek 3"])
    renk = st.color_picker("Favori renginizi seçin")
    tarih = st.date_input("Bir tarih seçin")

    if isim:
        st.success(f"Hoş geldin, {isim}!")  # Başarı mesajı

    # Checkbox ve Buton
    st.subheader("Etkinlik Onayı")
    etkinlik_onay = st.checkbox("Etkinliğe katılacak mısınız?")
    if etkinlik_onay:
        st.success("Harika! Seni etkinlikte görmek için sabırsızlanıyoruz.")

    buton = st.button("Bilgileri Gönder")
    if buton:
        st.write(f"Seçilen seçenek: {secim}")
        st.write(f"Favori renk: {renk}")
        st.write(f"Seçilen tarih: {tarih}")

    # Slider
    st.subheader("Bir Değer Seçin")
    deger = st.slider("Değeri seçin", 0, 100, 50)
    st.write(f"Seçilen değer: {deger}")

    # Harita ekleme
    st.subheader("Konum Haritası")
    harita_verisi = {"lat": [41.0082], "lon": [28.9784]}  # İstanbul koordinatları
    st.map(harita_verisi)