from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
import os

load_dotenv()


def gmail_credentials():

    creds = Credentials(
        token=None,
        refresh_token=os.getenv(
            "GMAIL_REFRESH_TOKEN"
        ),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv(
            "GMAIL_CLIENT_ID"
        ),
        client_secret=os.getenv(
            "GMAIL_CLIENT_SECRET"
        )
    )

    return creds
