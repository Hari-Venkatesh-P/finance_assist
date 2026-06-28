
from fastapi import HTTPException

from helpers.chat_utils import chat

def query_rag(question):
    try:
        answer = chat(question=question)
        return {
            "success": True,
            "data": answer,
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": "Failed to get answer",
            },
        )
