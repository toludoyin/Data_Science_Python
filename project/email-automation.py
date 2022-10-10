import os
from dotenv import load_dotenv
from email.message import EmailMessage
# import ssl
import smtplib

load_dotenv()

EMAIL_USER = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASS = os.environ.get('EMAIL_PASSWORD')
RECEIVER = os.environ.get('RECIPIENT')

msg = EmailMessage()
msg['Subject'] = "Test Email"
msg['From'] = EMAIL_USER
msg['To'] = RECEIVER
msg.set_content(' Hey! Toludoyin. This is a test email.')

# context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  #context=context
    smtp.login(EMAIL_USER, EMAIL_PASS)
    smtp.send_message(msg)