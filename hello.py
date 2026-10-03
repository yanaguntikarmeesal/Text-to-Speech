
import streamlit as st
from gtts import gTTS
import os

# ==============================================================
# 🎙️ AI VOCALIST - TEXT TO SPEECH
# ==============================================================

st.set_page_config(
    page_title="AI Vocalist",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================
# 🎨 CUSTOM CSS
# ==============================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap'
);

/* ============================================================
   🌈 BACKGROUND
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255,75,75,.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(168,85,247,.16),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(99,102,241,.14),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #f7f9fc,
            #e9edf5
        );

    font-family: 'Inter', sans-serif;
}

/* ============================================================
   🚫 HIDE STREAMLIT DEFAULT UI
   ============================================================ */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ============================================================
   📦 MAIN CONTAINER
   ============================================================ */

.block-container {
    max-width: 900px !important;
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}

/* ============================================================
   🪟 MAIN CARD
   ============================================================ */

.main .block-container {

    background: rgba(255,255,255,.97);

    border-radius: 30px;

    box-shadow:
        0 30px 70px rgba(30,43,58,.20),
        0 10px 30px rgba(30,43,58,.10);

    padding: 35px !important;

}

/* ============================================================
   🎙️ TITLE
   ============================================================ */

.hero-title {

    text-align: center;

    font-size: 3rem !important;

    font-weight: 900 !important;

    color: #ff4b4b !important;

    margin-bottom: 5px !important;

    text-shadow:
        0 5px 20px rgba(255,75,75,.15);

}

.hero-subtitle {

    text-align: center;

    font-size: 1.05rem;

    color: #64748b;

    margin-bottom: 30px;

}

/* ============================================================
   🎙️ MICROPHONE ICON
   ============================================================ */

.mic-icon {

    display: inline-block;

    font-size: 3.2rem;

    animation: micPulse 2s infinite;

}

@keyframes micPulse {

    0%,100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.15);
    }

}

/* ============================================================
   🎵 ICON CARDS
   ============================================================ */

.icon-card {

    background:
        linear-gradient(
            135deg,
            #ff4b4b,
            #a855f7
        );

    color: white;

    border-radius: 14px;

    padding: 10px;

    text-align: center;

    font-size: 22px;

    box-shadow:
        0 7px 18px rgba(255,75,75,.20);

}

/* ============================================================
   🏷️ STREAMLIT LABELS
   ============================================================ */

label {

    font-weight: 800 !important;

    color: #263445 !important;

    font-size: .90rem !important;

}

/* ============================================================
   🔽 SELECTBOX
   ============================================================ */

div[data-baseweb="select"] > div {

    border-radius: 16px !important;

    border: 2px solid #e2e8f0 !important;

    background: white !important;

    min-height: 48px;

    transition: .25s;

}

div[data-baseweb="select"] > div:hover {

    border-color: #ff4b4b !important;

    box-shadow:
        0 5px 18px rgba(255,75,75,.12) !important;

}

/* ============================================================
   ✏️ TEXT INPUT
   ============================================================ */

.stTextInput input {

    border-radius: 16px !important;

    border: 2px solid #e2e8f0 !important;

    padding: 13px 16px !important;

    font-size: 1rem !important;

    transition: .25s;

}

.stTextInput input:focus {

    border-color: #ff4b4b !important;

    box-shadow:
        0 0 0 4px rgba(255,75,75,.10) !important;

}

/* ============================================================
   📝 TEXT AREA
   ============================================================ */

.stTextArea textarea {

    border-radius: 20px !important;

    border: 2px solid #e2e8f0 !important;

    padding: 18px !important;

    font-size: 1rem !important;

    line-height: 1.6 !important;

    transition: .25s;

}

.stTextArea textarea:focus {

    border-color: #ff4b4b !important;

    box-shadow:
        0 0 0 4px rgba(255,75,75,.10) !important;

}

/* ============================================================
   🚀 GENERATE BUTTON
   ============================================================ */

.stButton > button {

    width: 100% !important;

    height: 58px !important;

    border-radius: 50px !important;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #ff3d3d,
            #ff6b6b,
            #a855f7
        ) !important;

    color: white !important;

    font-size: 1.15rem !important;

    font-weight: 800 !important;

    box-shadow:
        0 12px 30px rgba(255,75,75,.35);

    transition: .3s;

}

.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 18px 35px rgba(255,75,75,.45);

}

/* ============================================================
   📥 DOWNLOAD BUTTON
   ============================================================ */

.stDownloadButton > button {

    width: 100% !important;

    height: 52px !important;

    border-radius: 50px !important;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #1e293b,
            #334155
        ) !important;

    color: white !important;

    font-weight: 700 !important;

    font-size: 1rem !important;

    transition: .3s;

}

.stDownloadButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 25px rgba(15,23,42,.30);

}

/* ============================================================
   🔊 AUDIO
   ============================================================ */

div[data-testid="stAudio"] {

    background:
        linear-gradient(
            135deg,
            #fff5f5,
            #f4f1ff
        );

    border-radius: 20px;

    padding: 10px;

    border: 1px solid #f1dada;

}

/* ============================================================
   ⚠️ ALERTS
   ============================================================ */

div[data-testid="stAlert"] {

    border-radius: 16px !important;

    border: none !important;

    box-shadow:
        0 8px 20px rgba(0,0,0,.06);

}

/* ============================================================
   📱 MOBILE
   ============================================================ */

@media(max-width:640px) {

    .block-container {

        padding: 20px !important;

    }

    .hero-title {

        font-size: 2.2rem !important;

    }

    .mic-icon {

        font-size: 2.4rem;

    }

}

</style>
""", unsafe_allow_html=True)


# ==============================================================
# 🎙️ HERO SECTION
# ==============================================================

st.markdown(
    '<h1 class="hero-title">'
    '🎙️ AI Vocalist'
    '</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="hero-subtitle">'
    '✨ Transform your text into natural-sounding speech '
    'using AI-powered text-to-speech technology.'
    '</p>',
    unsafe_allow_html=True
)


# ==============================================================
# 🌍 LANGUAGE DATA
# ==============================================================

languages = {
    "🇮🇳 Hindi": "hi",
    "🇬🇧 English": "en",
    "🇮🇳 Kannada": "kn",
    "🇪🇸 Spanish": "es",
    "🇫🇷 French": "fr",
    "🇩🇪 German": "de",
    "🇯🇵 Japanese": "ja",
    "🇨🇳 Chinese": "zh-cn"
}


# ==============================================================
# 🌍 LANGUAGE + FILE NAME
# ==============================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🌍 Select Language")

    selected_lang_name = st.selectbox(
        "Language",
        list(languages.keys()),
        label_visibility="collapsed"
    )

    lang_code = languages[selected_lang_name]


with col2:

    st.markdown("### 📁 Audio Filename")

    user_filename = st.text_input(
        "Filename",
        placeholder="my_speech",
        label_visibility="collapsed"
    )


# ==============================================================
# ✍️ TEXT INPUT
# ==============================================================

st.markdown("### ✍️ Enter Your Text")

text = st.text_area(
    "Text",
    placeholder=f"✨ Type something in {selected_lang_name} here...",
    height=170,
    label_visibility="collapsed"
)


# ==============================================================
# 🚀 GENERATE AUDIO
# ==============================================================

if st.button("🎙️ Generate AI Voice"):

    if text.strip():

        base_name = (
            user_filename.strip()
            if user_filename.strip()
            else "speech_output"
        )

        full_filename = f"{base_name}.mp3"

        try:

            with st.spinner(
                f"🎧 Creating {selected_lang_name} audio..."
            ):

                tts = gTTS(
                    text=text,
                    lang=lang_code,
                    slow=False
                )

                tts.save(full_filename)


            st.success(
                "✨ Your AI voice has been created successfully!"
            )


            # ==================================================
            # 🔊 GENERATED AUDIO
            # ==================================================

            st.markdown("### 🔊 Generated Audio")

            st.audio(
                full_filename,
                format="audio/mp3"
            )


            # ==================================================
            # 📥 DOWNLOAD
            # ==================================================

            with open(full_filename, "rb") as file:

                st.download_button(
                    label="📥 Download MP3 Audio",
                    data=file,
                    file_name=full_filename,
                    mime="audio/mp3"
                )


        except Exception as e:

            st.error(
                f"❌ Error: {e}. "
                "Please check your internet connection."
            )

    else:

        st.warning(
            "⚠️ Please enter some text before generating audio."
        )


# ==============================================================
# 👨‍💻 FOOTER
# ==============================================================

st.divider()

st.caption(
    "🎙️ AI Vocalist | "
    "Developed by Yanaguntikar Meesal | "
    "🚀 Streamlit + Google TTS"
)


# ==============================================================
# INSTALL
# ==============================================================

# python -m pip install streamlit gTTS
# python -m streamlit run app.py

