import streamlit as st
import requests

st.set_page_config(page_title="GLC Motion & Logo Generator", page_icon="🎨", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #121212; color: #FFFFFF; }
    h1, h2, h3 { color: #0061A4 !important; }
    .stButton>button { background-color: #0061A4; color: white; width: 100%; border-radius: 8px; }
    </style>
    """, unsafe_allowed_html=True)

st.title("🎨 GLC MOTION & LOGO")
st.subheader("Creative Generator")
st.write("---")

menu = st.sidebar.selectbox("MENU", ["Logo Studio", "Video Lab"])

if menu == "Logo Studio":
    st.header("✨ Logo Studio")
    brand_name = st.text_input("Company Name / Brand Title :", value="GLC Entertainment")
    tagline = st.text_input("Tagline / Slogan (Optional) :", placeholder="e.g., Creative Vision")
    logo_style = st.selectbox("Minimalist Logo Style :", ["Geometric luxury brand", "Line Art", "Monogram", "Negative Space", "Flat Icon"])
    color_palette = st.selectbox("Primary Color Palette :", ["Blue & White", "Black & Gold", "Minimalist Black", "Neon Glow"])

    if st.button("Generate Minimal Logo ✨"):
        with st.spinner("GLC Engine ကနေ ပုံဖော်ပေးနေပါတယ်... ခဏစောင့်ပါ..."):
            try:
                final_prompt = f"A professional minimalist logo, {logo_style} style, text with '{brand_name}', tagline '{tagline}', color theme {color_palette}, high resolution vector graphic, masterpiece, clean background"
                api_url = f"https://image.pollinations.ai/p/{requests.utils.quote(final_prompt)}?width=1024&height=1024&enhance=true"
                st.success("Logo Generated Successfully!")
                st.image(api_url, caption=f"Crafted for {brand_name}", use_container_width=True)
            except Exception as e:
                st.error(f"Error: {e}")

elif menu == "Video Lab":
    st.header("🎬 Video Lab")
    st.info("💡 Video Concept generator is ready for connection.")
    video_prompt = st.text_area("ဗီဒီယိုထဲမှာ ဖြစ်ပျက်စေချင်တဲ့ အိုင်ဒီယာကို ရေးပါ :", placeholder="e.g., Cinematic camera pan of a flying crane...")
    if st.button("Generate Video Motion 🎥"):
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
