from fastapi import APIRouter
from helpers.query_request import QueryRequest
from service.chat_service import query_rag

router = APIRouter(prefix="/chat")


@router.post("")
async def search(request: QueryRequest):
    return query_rag(request.query)
