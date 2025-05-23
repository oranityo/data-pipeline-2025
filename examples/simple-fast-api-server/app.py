from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    print("healthy")
    return {"message": "all good"}
