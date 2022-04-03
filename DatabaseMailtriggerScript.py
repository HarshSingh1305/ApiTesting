from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib


def send_mail():
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = 'GetDataAnytime'
    msg['From'] = 'dailygenixauto@gmail.com'
    msg['To'] = 'msdhamija@yahoo.co.in,harshdhiman01@gmail.com'
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open('/__w/ApiTesting/ApiTesting/getDataAnytime.csv','rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=FILE_NAME))

    # Create SMTP object
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    # Login to the server
    smtp_obj.login('dailygenixauto@gmail.com', 'H@rshsingh1305')

    # Convert the message to a string and send it
    smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp_obj.quit()
