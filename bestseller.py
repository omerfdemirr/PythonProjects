import requests as rq
import xml.etree.ElementTree as et
import streamlit as st

# Veri çekme
r = rq.get("https://www.nytimes.com/sitemaps/new/best-sellers.xml")
veri = r.content
root = et.fromstring(veri)

# Kitap isimlerini saklayacak liste
kitap_listesi = []

for x in root:
    try:
        loc = x[0].text  # İlk elemanı al
        isim = loc.split("/")[-2]  # URL'den kitabın adını al
        isim = isim.replace("-", " ")  # "-" karakterlerini boşlukla değiştir
        isim = isim.title()  # İlk harfleri büyük yap
        kitap_listesi.append(isim)  # Listeye ekle
    except IndexError:
        continue  # Eğer x[0] yoksa, hatayı geç


kitap_listesi=sorted(kitap_listesi)
st.title("NY Times En Çok Satanlar Listesi")
secilen_kitap = st.selectbox("Bir kitap seçin:", kitap_listesi)


st.write(f"Seçilen Kitap: {secilen_kitap}")


st.write(f"Toplam Kitap Sayısı: {len(kitap_listesi)}")