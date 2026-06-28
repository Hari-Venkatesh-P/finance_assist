from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

from routers.email_router import router as email_router
from routers.injestion_router import router as injestion_router

load_dotenv()

app = FastAPI()

@app.get("/health")
def health():
    return JSONResponse(
        status_code=200, content={"status": "UP", "message": "Application is healthy"}
    )


app.include_router(email_router)
app.include_router(injestion_router)

