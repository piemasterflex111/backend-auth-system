from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend system running"}

@app.get("/health")
def health():
    return {"status": "ok"}