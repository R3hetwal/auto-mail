import smtplib
import email.utils
import ssl
from rt import mail
from time import sleep

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "......@gmail.com"
password = input("enter your password:")
recived = mail

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email

def _send():
    server = smtplib.SMTP("smtp.gmail.com" ,587)
    server.ehlo()# Can be omitted
    server.starttls(context=context)# Secure the connection
    
    server.login(sender_email, password)
    subject = "Hey there!"
    body = "just try"

    msg = f"subject:{subject} \n\n {body}"
    server.sendmail(sender_email, recived, msg)
    print("hey email sented")
    server.quit()

x=0
for I in range(5):
    _send()
    sleep(60)


# server.quit()
