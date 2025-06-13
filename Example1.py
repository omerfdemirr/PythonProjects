import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Jarvis",layout="centered")

st.title("Jarvis")
st.write("Selam Patron Ben Jarvis")

komut=st.text_input("Emirleriniz(saat,şaka,sözler)")

if komut:
    komut=komut.lower()

    if "saat" in komut:
        st.success(f"⏰ Şu an saat: {datetime.now().strftime('%H:%M')}")

    elif "şaka" in komut:
        şakalar=[
            " :)))"

        ]
        st.info(random.choice(şakalar))

    elif "motive" in komut:
        sözler=[
            ""
        ]
        st.info(random.choice(sözler))

    else:
        st.warning("Hatalı Giriş Yaptınız")