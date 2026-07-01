import streamlit as st
import tempfile

from backend.detector import detect_food
from backend.nutrition_engine import calculate_nutrition

st.set_page_config(page_title="NutriSense Vision AI")

st.title("🍎 NutriSense Vision AI")

uploaded_file = st.file_uploader(
    "Upload Food Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(uploaded_file, caption="Uploaded Image")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        image_path = temp_file.name

    # Detect food
    detections = detect_food(image_path)

    # Calculate nutrition
    nutrition = calculate_nutrition(detections)

    # Display detected foods
    st.subheader("🍽 Detected Items")

    if detections:
        for item in detections:
            st.write(
                f"**{item['name']}** ({item['confidence']*100:.1f}%)"
            )
    else:
        st.warning("No food detected.")

    # Nutrition Summary
    st.subheader("📊 Nutrition Summary")

    st.metric("Calories", f"{nutrition['calories']} kcal")

    col1, col2, col3 = st.columns(3)

    col1.metric("Protein", f"{nutrition['protein']:.1f} g")
    col2.metric("Carbs", f"{nutrition['carbs']:.1f} g")
    col3.metric("Fat", f"{nutrition['fat']:.1f} g")