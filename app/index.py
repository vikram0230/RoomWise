from fastapi import FastAPI
from app.routes import user

app = FastAPI()
app.include_router(user)

# uvicorn app.index:app --reload
# mongodb://localhost:27017/