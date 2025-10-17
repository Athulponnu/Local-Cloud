from fastapi import FastAPI

app = FastAPI(title="Hybrid Cloud-Based Intelligent Image Analysis System")

@app.get("/")
def home():
    return {"message": "Welcome to the Hybrid Cloud AI API!"}
