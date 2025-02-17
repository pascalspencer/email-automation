import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv('SENDER')
receiver = os.getenv('RECEIVER')  
subject = 'EMAIL AUTOMATION'
password = os.getenv('PASSWORD')

email = EmailMessage()
email['From'] = 'Spencer LTD'
email['To'] = receiver
email['Subject'] = subject

email.set_content('This is an automation using python')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(email)
        print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
