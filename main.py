from fastapi import FastAPI
from routes import auth, posts

app = FastAPI()

@app.get("/", tags=["health-check"])
def home():
    return {"message": "Server Running 🏃"}


app.include_router(auth.router)
app.include_router(posts.router)