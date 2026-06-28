import re
import uuid
import os
from service.gmail_service import get_emails
from langchain_core.documents import Document
from helpers.utils import email_to_embedding_text, create_faiss_index

from fastapi import HTTPException


def injest_data():
    try:
        emails = get_emails()

        docs = []
        for email in emails:
            text = email_to_embedding_text(email)

            if text and len(text) > 0:
                docs.append(Document(page_content=text))

        create_faiss_index(docs)

        return {
            "success": True,
            "message": "FAISS index created successfully",
            "emails_processed": len(emails),
            "documents_indexed": len(docs),
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": "Failed to create FAISS index",
                "error": str(e),
            },
        )
