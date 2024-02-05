from email.message import EmailMessage
import ssl 
import smtplib 

email_sender = "Account signed in as"
email_password = "Your App Password"
email_reciever = ['a@gmail.com', 'b0@gmail.com', 'c@gmail.com'] 
subject = "Example Subject"
body = """Example Body"""

em = EmailMessage()
em['From'] = email_sender 
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: # (Email server, port, context)
    smtp.login(email_sender, email_password)
    for email in email_reciever: 
        smtp.sendmail(email_sender, email, em.as_string())
        

print("Sent Emails")