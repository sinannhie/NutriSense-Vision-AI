import streamlit as st

st.set_page_config(
    page_title="NutriSense Vision AI"
)

st.title("🍎 NutriSense Vision AI")

uploaded_file = st.file_uploader(
    "Upload Food Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    st.image(
        uploaded_file,
        caption="Uploaded Image"
    )