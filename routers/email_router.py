from fastapi import APIRouter
from service.gmail_service import get_emails

router = APIRouter(prefix="/email")

@router.get("")
async def emails():
    return get_emails()
