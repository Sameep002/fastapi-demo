from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
def read_root():
    sample = "This is fastapi endpoint"
    return sample
