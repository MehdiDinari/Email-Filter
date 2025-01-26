import streamlit as st
from SpamDetection import predict_and_save

st.set_page_config(page_title="Spam Detector", page_icon="📩", layout="centered")

st.title("📩 Spam Detection App")

st.markdown("""
Entrez un message et vérifiez s'il est **Spam** ou **Non Spam** grâce à un modèle **Naïve Bayes**.
""")

message = st.text_area("✍️ **Entrez votre message ici**:", height=100)

if st.button("🔍 Prédire"):
    if message.strip() == "":
        st.warning("Veuillez entrer un message avant de prédire.")
    else:
        result = predict_and_save(message)
        if result == "Spam":
            st.error(f"🚨 **Ce message est classé comme SPAM !**")
        else:
            st.success(f"✅ **Ce message est classé comme NON SPAM.**")

st.markdown("""
---
📌 **Projet développé avec** `Streamlit`, `Scikit-learn` et `SQLite`.  
💡 **Modèle utilisé** : Naïve Bayes avec `CountVectorizer`
""")
