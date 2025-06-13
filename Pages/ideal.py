import streamlit as st

# Başlık
st.title("Vücut Kitle İndeksi (BMI) Hesaplama")

# Kullanıcının boy ve kilo bilgilerini girmesi
boy = st.number_input("Boyunuzu girin (metre cinsinden):", min_value=0.5, max_value=2.5, step=0.01)
kilo = st.number_input("Kilonuzu girin (kg cinsinden):", min_value=10.0, max_value=300.0, step=0.5)

# BMI hesaplama
if boy > 0 and kilo > 0:
    bmi = kilo / (boy ** 2)
    st.write(f"**Vücut Kitle İndeksiniz (BMI):** {bmi:.2f}")

    # BMI kategorileri
    if bmi < 18.5:
        st.warning("Sonuç: **Zayıf**. Daha fazla beslenmeye dikkat etmelisiniz.")
    elif 18.5 <= bmi < 24.9:
        st.success("Sonuç: **İdeal**. Sağlıklı bir kiloya sahipsiniz!")
        
    elif 25 <= bmi < 29.9:
        st.warning("Sonuç: **Fazla Kilolu**. Dikkatli olmalısınız.")
    else:
        st.error("Sonuç: **Obez**. Sağlıklı yaşam için uzman görüşü almanızı öneririm.")