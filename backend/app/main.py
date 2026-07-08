from fastapi import FastAPI

app = FastAPI(
    title="AI Career Agent",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "AI Career Agent",
        "version": "0.1.0",
        "status": "running"
    }