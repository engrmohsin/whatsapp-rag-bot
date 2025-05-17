from fastapi import FastAPI, Request, Form
from twilio.rest import Client
import os

app = FastAPI()

# Initialize Twilio client with environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')  # e.g. 'whatsapp:+14155238886'

client = Client(account_sid, auth_token)

@app.post("/webhook")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...)
):
    # Here is where you can add your RAG logic to process Body and generate a reply
    user_msg = Body.strip()

    # For demo, just echo the message back with a prefix
    reply_text = f"RAG bot says: You sent -> {user_msg}"

    # Send reply back to user via Twilio WhatsApp
    client.messages.create(
        from_=twilio_whatsapp_number,
        to=From,
        body=reply_text
    )

    return "OK"
