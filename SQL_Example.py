import streamlit as st
import sqlite3 as sq

conn = sq.connect('notlar.db', check_same_thread=False)
c = conn.cursor()


c.execute('''
CREATE TABLE IF NOT EXISTS notlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    baslik TEXT NOT NULL,
    icerik TEXT NOT NULL
)
''')
conn.commit()


def not_ekle(baslik, icerik):
    c.execute("INSERT INTO notlar (baslik, icerik) VALUES (?, ?)", (baslik, icerik))
    conn.commit()


def notları_getir():
    c.execute("SELECT * FROM notlar ORDER BY id DESC")
    return c.fetchall()


st.title("Not Defteri")
st.subheader(" Yeni Not Ekle")


baslik = st.text_input("Not Başlığı")
icerik = st.text_area("Not İçeriği")

if st.button("Notu Kaydet"):
    if baslik and icerik:
        not_ekle(baslik, icerik)
        st.success(" Not başarıyla kaydedildi!")
    else:
        st.warning(" Lütfen başlık ve içerik gir.")


st.subheader("Kayıtlı Notlar")

notlar = notları_getir()

if notlar:
    for not_id, baslik,icerik in notlar:
        with st.expander(f"{baslik}"):
            st.write(icerik)

    else:
        st.info("Henüz kayıt yok")