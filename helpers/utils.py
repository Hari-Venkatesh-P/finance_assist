from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import base64, re
from bs4 import BeautifulSoup


def html_to_text(html) -> str:
    return BeautifulSoup(html, "html.parser").get_text(separator=" ", strip=True)

def extract_email_body(part):

    if not part:
        return ""

    mime_type = part.get("mimeType", "")

    body = part.get("body", {})
    data = body.get("data")

    # Prefer text/plain
    if mime_type == "text/plain" and data:
        return base64.urlsafe_b64decode(data.encode()).decode("utf-8", errors="ignore")

    # Fallback to html
    if mime_type == "text/html" and data:
        return html_to_text(base64.urlsafe_b64decode(data.encode()).decode("utf-8", errors="ignore"))

    # Recursively search children
    for child in part.get("parts", []):

        result = extract_email_body(child)

        if result:
            return result

    return ""


def email_to_embedding_text(email) -> str:

    if email is None:
        return ""

    text = ""
    email_body = email["payload"]
    try:
        text = extract_email_body(email_body)
    except Exception:
        text = email.get("snippet", "Unknown")

    return re.sub(r"\s+", " ", text).strip()


def create_faiss_index(docs):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("finance_index")
