from fastapi import FastAPI
from api.routes import user

app = FastAPI()
app.include_router(user)

# uvicorn index:app --reload
# mongodb://localhost:27017/