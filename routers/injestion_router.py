from fastapi import APIRouter
from service.injestion_service import injest_data

router = APIRouter(prefix="/injest")

@router.get("")
async def injest():
    return injest_data()
