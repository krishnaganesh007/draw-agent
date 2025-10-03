# # gmail_sender.py
# import os
# import base64
# from email.message import EmailMessage

# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# def _get_creds(client_secret_path="client_secret.json", token_path="token.json"):
#     creds = None
#     if os.path.exists(token_path):
#         creds = Credentials.from_authorized_user_file(token_path, SCOPES)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open(token_path, "w") as f:
#             f.write(creds.to_json())
#     return creds

# def _build_service(creds):
#     return build("gmail", "v1", credentials=creds)

# def _encode_message(msg: EmailMessage) -> dict:
#     raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
#     return {"raw": raw}

# def send_gmail_text(sender: str, to: str, subject: str, body_text: str,
#                     client_secret_path="client_secret.json", token_path="token.json"):
#     """Send a plain-text email via Gmail API."""
#     creds = _get_creds(client_secret_path, token_path)
#     service = _build_service(creds)
#     msg = EmailMessage()
#     msg["From"] = sender
#     msg["To"] = to
#     msg["Subject"] = subject
#     msg.set_content(body_text)
#     body = _encode_message(msg)
#     try:
#         resp = service.users().messages().send(userId="me", body=body).execute()
#         return resp
#     except HttpError as e:
#         raise RuntimeError(f"Gmail send failed: {e}")

# def send_gmail_html(sender: str, to: str, subject: str, html_body: str,
#                     client_secret_path="client_secret.json", token_path="token.json",
#                     attachments: list[str] | None = None):
#     """Send an HTML email; optional attachments list of file paths."""
#     creds = _get_creds(client_secret_path, token_path)
#     service = _build_service(creds)
#     msg = EmailMessage()
#     msg["From"] = sender
#     msg["To"] = to
#     msg["Subject"] = subject
#     msg.set_content("This email contains HTML content.")
#     msg.add_alternative(html_body, subtype="html")
#     if attachments:
#         import mimetypes, pathlib
#         for path in attachments:
#             p = pathlib.Path(path)
#             ctype, _ = mimetypes.guess_type(p.name)
#             maintype, subtype = (ctype or "application/octet-stream").split("/", 1)
#             with open(p, "rb") as f:
#                 msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=p.name)
#     body = _encode_message(msg)
#     try:
#         resp = service.users().messages().send(userId="me", body=body).execute()
#         return resp
#     except HttpError as e:
#         raise RuntimeError(f"Gmail send failed: {e}")
    

# # from gmail_sender import send_gmail_text

# final_text = "Final result: 123.45\nRendered on AutoDraw successfully."
# resp = send_gmail_text(
#     sender="ytscientist.krishna@gmail.com",
#     to="ganesh.krishnaganesh@gmail.com",
#     subject="[Agent] Final result",
#     body_text=final_text
# )
# print("Sent message id:", resp.get("id"))


# creds = _get_creds(client_secret_path="client_secret.json", token_path="token.json")
# service = _build_service(creds)

import os
import base64
from email.message import EmailMessage

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def main():
    # Point to your downloaded OAuth client file
    CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET_PATH", "client_secret.json")
    if not os.path.exists(CLIENT_SECRET):
        raise FileNotFoundError(f"Missing OAuth client file: {CLIENT_SECRET}")

    # 1) Interactive OAuth once; token is cached locally
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
    creds = flow.run_local_server(port=0)

    # 2) Build Gmail service
    service = build("gmail", "v1", credentials=creds)

    # 3) Compose message
    sender = os.getenv("GMAIL_SENDER", "me")  # "me" uses the authorized account
    to = os.getenv("GMAIL_TO", "priyankadantala123@gmail.com") #"ganesh.krishnaganesh@gmail.com"
    subject = "Gmail API test"
    body = "Hello from the Gmail API via Python."

    msg = EmailMessage()
    msg["To"] = to
    msg["From"] = sender
    msg["Subject"] = subject
    msg.set_content(body)

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")
    message_body = {"raw": raw}

    # 4) Send
    try:
        resp = service.users().messages().send(userId="me", body=message_body).execute()
        print("Sent. Message Id:", resp.get("id"))
    except HttpError as e:
        print("Gmail send failed:", e)

if __name__ == "__main__":
    main()
