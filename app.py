import streamlit as st
from gtts import gTTS
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Vocalist", page_icon="🎙️", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .stTextArea textarea { border-radius: 15px; }
    .stTextInput input { border-radius: 10px; }
    h1 { text-align: center; color: #FF4B4B; font-family: 'Arial Black', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎙️  Text-to-Speech")
st.write("Convert your text into natural-sounding speech in multiple languages.")

# --- DATA ---
languages = {
    "Hindi": "hi",
    "English": "en",
    "Kannada": "kn",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-cn"
}

# --- UI LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    selected_lang_name = st.selectbox("1. Select Language", list(languages.keys()))
    lang_code = languages[selected_lang_name]

with col2:
    user_filename = st.text_input("2. Filename (Optional)", placeholder="my_speech")

# Using a key for the text area to allow for clearing later
text = st.text_area("3. Enter Text", placeholder=f"Type something in {selected_lang_name} here...", height=150)

st.markdown("---")

# --- CONVERSION LOGIC ---
if st.button("🚀 Generate Audio"):
    if text.strip():
        # Clean filename
        base_name = user_filename.strip() if user_filename.strip() else "speech_output"
        full_filename = f"{base_name}.mp3"

        try:
            with st.spinner(f"Processing {selected_lang_name} Audio..."):
                # The lang=lang_code ensures Hindi selection results in Hindi audio
                tts = gTTS(text=text, lang=lang_code, slow=False)
                tts.save(full_filename)

            st.success(f"✨ Created successfully!")

            # Display Audio Player
            st.audio(full_filename, format="audio/mp3")

            # Download Button
            with open(full_filename, "rb") as file:
                st.download_button(
                    label="📥 Download MP3",
                    data=file,
                    file_name=full_filename,
                    mime="audio/mp3"
                )

        except Exception as e:
            st.error(f"Error: {e}. Please ensure you have an active internet connection.")
    else:
        st.warning("⚠️ Please provide some text first.")

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Developed by **Yanaguntikar Meesal** | Built with Streamlit & Google TTS")

# python -m pip install streamlit gTTS
# python -m streamlit run app.py