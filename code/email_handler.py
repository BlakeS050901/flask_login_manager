from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

sender_email = os.environ.get('EMAIL')
password = os.environ.get('EMAIL_PASSWORD')

def code_send(email, code):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = 'Password Reset Code'

    body = f'Your password reset code is: {code}'
    message.attach(MIMEText(body, 'plain'))

    server = SMTP('smtp.office365.com', 587)
    try:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message.as_string())
        print('Email sent')
        response = True
    except Exception as e:
        print(f"Error: {e}")
        response = False
        pass
    finally:
        server.quit()
        return response


