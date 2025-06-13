import streamlit as st

# Başlık
st.title("Akbil Bakiye ve Kullanım Uygulaması")

# Varsayılan başlangıç bakiyesi
if "bakiye" not in st.session_state:
    st.session_state.bakiye = 50.0  # Başlangıçta 50 TL bakiye

# Kullanıcının mevcut bakiyesini göster
st.write(f"**Mevcut Bakiyeniz:** {st.session_state.bakiye:.2f} TL")

# Bakiye yükleme
yukleme_miktari = st.number_input("Yüklemek istediğiniz miktarı girin:", min_value=1.0, step=1.0)
if st.button("Bakiye Yükle"):
    st.session_state.bakiye += yukleme_miktari
    st.success(f"{yukleme_miktari:.2f} TL yüklendi! Yeni bakiyeniz: {st.session_state.bakiye:.2f} TL")

# Yolculuk yapma
yolculuk_ucreti = 9.90  # Varsayılan yolculuk ücreti
if st.button("Yolculuk Yap"):
    if st.session_state.bakiye >= yolculuk_ucreti:
        st.session_state.bakiye -= yolculuk_ucreti
        st.success(f"Yolculuk tamamlandı! Yeni bakiyeniz: {st.session_state.bakiye:.2f} TL")
    else:
        st.error("Yetersiz bakiye! Lütfen bakiye yükleyin.")

# Güncellenmiş bakiyeyi göster
st.write(f"**Güncellenmiş Bakiyeniz:** {st.session_state.bakiye:.2f} TL")