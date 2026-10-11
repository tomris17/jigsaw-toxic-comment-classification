import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Jigsaw Toxic Comment Classification",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Jigsaw Toxic Comment Classification")
st.write("Bu arayüz, girilen bir yorumun toksisite oranını analiz ederek içerik denetimi yapmanızı sağlar.")

user_comment = st.text_area("Yorumunuzu Yazın:", "You are doing an amazing job, keep it up!")

if st.button("Analiz Et"):
    if not user_comment.strip():
        st.warning("Lütfen geçerli bir metin girin.")
    else:
        # Basit kural tabanlı simülasyon veya eğitilen model tahmin arayüzü
        toxic_words = ["idiot", "stupid", "hate", "worst", "damn", "trash"]
        is_toxic = any(word in user_comment.lower() for word in toxic_words)
        
        st.markdown("---")
        st.subheader("📊 Analiz Sonucu:")
        if is_toxic:
            st.error("⚠️ **TOKSLİK ALGILANDI** (Bu yorum hakaret veya saldırgan ifadeler içerebilir.)")
        else:
            st.success("✅ **GÜVENLİ / TEMİZ İÇERİK** (Herhangi bir toksisite tespit edilmedi.)")