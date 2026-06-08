from fastapi import FastAPI

app = FastAPI(
    title="NutriSense Vision AI"
)

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "NutriSense Vision AI"
    }