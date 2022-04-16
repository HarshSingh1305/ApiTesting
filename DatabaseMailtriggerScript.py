import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "dailygenixauto@gmail.com"
APP_PASSWORD = "H@rshsingh1305"

def send_mail_with_excel(recipient_email, subject, content, excel_file):
    msg = EmailMessage()
    msg['Subject'] = "GetDataAnytime"
    msg['From'] = "dailygenixauto@gmail.com"
    msg['To'] = "harshdhiman01@gmail.com,msdhamija@yahoo.co.in"
    msg.set_content(content)

    with open(excel_file, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=getDataAnytime.csv)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
