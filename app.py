from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routers.email_router import router as email_router
from routers.injestion_router import router as injestion_router
from routers.chat_router import router as chat_router

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return JSONResponse(
        status_code=200, content={"status": "UP", "message": "Application is healthy"}
    )

app.include_router(email_router)
app.include_router(injestion_router)
app.include_router(chat_router)

