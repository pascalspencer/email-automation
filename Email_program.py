import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime  # Import datetime to include timestamp in the message

# Load environment variables from .env file
load_dotenv()

# Fetch sender email, receiver email, and password from environment variables
sender = os.getenv('SENDER')
receiver = os.getenv('RECEIVER')  
password = os.getenv('PASSWORD')

# Define email subject
subject = 'EMAIL AUTOMATION REMINDER'

# Get current timestamp
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Create email message instance
email = EmailMessage()
email['From'] = sender  # Use the sender's actual email
email['To'] = receiver  # Set recipient email
email['Subject'] = subject  # Set subject line

# Set email content with timestamp and sender information
email.set_content(f"Hello,\n\nThis is a reminder email sent via automation.\n\nSent by: {sender}\nTime: {current_time}\n\nBest Regards,\nAutomated System")

try:
    # Establish SMTP connection to Gmail's SMTP server
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()  # Identify with the server
        smtp.starttls()  # Secure the connection
        smtp.login(sender, password)  # Login to the sender email account
        smtp.send_message(email)  # Send the email
        print(f'Email sent successfully at {current_time}!')  # Print success message with timestamp
except Exception as e:
    # Print error message in case of failure
    print(f'Error: {e}')
