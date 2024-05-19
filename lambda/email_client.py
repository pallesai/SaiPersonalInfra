from email.message import EmailMessage

import smtplib

def send_email(subject, body, sender, recipients, password):

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg.set_content(body, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.ehlo()
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        smtp_server.close()
        print("Message sent!")