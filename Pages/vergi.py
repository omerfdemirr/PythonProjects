import streamlit as st

# Başlık
st.title("Vergi Hesaplama Sistemi")

# Kullanıcının gelirini girmesi
kazanc = st.number_input("Lütfen kazancınızı girin:", min_value=0.0, step=1000.0)

# Vergi dilimleri
v158 = 158000 * 0.15
v330 = (330000 - 158000) * 0.20
v800 = (800000 - 330000) * 0.27
v4300 = (4300000 - 800000) * 0.35

# Vergi hesaplama
if kazanc <= 158000:
    vergi = kazanc * 0.15
elif kazanc <= 330000:
    vergi = v158 + ((kazanc - 158000) * 0.20)
elif kazanc <= 800000:
    vergi = v158 + v330 + ((kazanc - 330000) * 0.27)
elif kazanc <= 4300000:
    vergi = v158 + v330 + v800 + ((kazanc - 800000) * 0.35)
else:
    vergi = v158 + v330 + v800 + v4300 + ((kazanc - 4300000) * 0.40)

# Sonucu ekrana yazdır
st.write(f"**Ödenecek Vergi:** {vergi:.2f} TL")