# 🍎 NutriSense Vision AI

An AI-powered nutrition analysis platform that detects food items from images, estimates nutritional values, and provides personalized dietary insights using Computer Vision and Deep Learning.

---

## 🚀 Project Overview

NutriSense Vision AI aims to simplify meal tracking by allowing users to upload a food image instead of manually entering food items.

The system detects foods in the image, estimates nutritional values, and presents a nutrition summary through an interactive web interface.

This project is being developed as an end-to-end AI application showcasing Deep Learning, Computer Vision, Backend Development, and Data Engineering.

---

## ✨ Current Features (v0.1)

* 📷 Upload food images
* 🤖 Food detection using YOLOv8
* 🍎 Detect multiple food items
* 📊 Nutrition estimation (Calories, Protein, Carbs, Fat)
* 💻 Interactive Streamlit interface

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Computer Vision

* YOLOv8 (Ultralytics)
* OpenCV

### Backend

* FastAPI

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Database

* SQLite (Upcoming)

---

## 📂 Project Structure

```
NutriSense-Vision-AI/

├── backend/
│   ├── app.py
│   ├── detector.py
│   ├── nutrition_engine.py
│   ├── database.py
│   └── __init__.py
│
├── frontend/
│   ├── streamlit_app.py
│
├── data/
│   └── nutrition.csv
│
├── models/
├── notebooks/
├── screenshots/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/NutriSense-Vision-AI.git
```

Navigate to the project

```bash
cd NutriSense-Vision-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m streamlit run frontend/streamlit_app.py
```

---

## 📸 Current Workflow

```
Upload Image
      │
      ▼
YOLOv8 Detection
      │
      ▼
Detected Food Items
      │
      ▼
Nutrition Database
      │
      ▼
Calories & Macronutrients
      │
      ▼
Display Results
```

---

## 🔮 Planned Features

* Food-specific detection model
* Portion size estimation
* Meal history with SQLite
* Nutrition dashboard
* Weekly calorie tracking
* AI nutrition recommendations
* User authentication
* Cloud deployment

---

## 🎯 Future Roadmap

* Replace generic YOLO model with a food-specific detector
* Improve food recognition accuracy
* Add portion estimation
* Build nutrition analytics dashboard
* Deploy the application online

---

## 👨‍💻 Author

**Muhammed Sinan M**

Aspiring AI & Data Science Engineer passionate about Machine Learning, Deep Learning, and Computer Vision.
