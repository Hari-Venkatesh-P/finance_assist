from googleapiclient.discovery import build
from fastapi import HTTPException
import os

from helpers.gmail_auth import gmail_credentials


def gmail_client():
    return build("gmail", "v1", credentials=gmail_credentials())


def get_label_id(label_name):
    client = gmail_client()
    labels = client.users().labels().list(userId="me").execute().get("labels", [])
    for label in labels:
        if label["name"] == label_name:
            return label["id"]
    return None


def get_emails():
    try:
        client = gmail_client()
        response = (
            client.users()
            .messages()
            .list(
                userId="me",
                maxResults=100,
                q="newer_than:7d",
                labelIds=[get_label_id(os.getenv("LABEL_NAME"))],
            )
            .execute()
        )
        message_ids = response.get("messages", [])
        data = []
        for msg in message_ids:
            full_message = (
                client.users().messages().get(userId="me", id=msg["id"]).execute()
            )
            data.append(full_message)
        return {
            "success": True,
            "count": len(data),
            "data": data,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": "Failed to fetch emails",
                "error": str(e),
            },
        )
