from deep_translator import GoogleTranslator
import streamlit as st

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 CodeAlpha Language Translation Tool")
st.write("Translate text between multiple languages instantly")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

text = st.text_area("Enter text here:", height=150)

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Complete ✅")
        st.text_area("Translated Text:", translated, height=150)
    else:
        st.warning("Please enter some text first!")