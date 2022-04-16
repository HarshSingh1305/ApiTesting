import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def send_mail(send_from,send_to,subject,text,files,server,port,username='dailygenixauto@gmail.com',password='H@rshsingh1305',isTls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("getDataAnytime.csv", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="/__w/ApiTesting/ApiTesting/getDataAnytime.csv"')
    msg.attach(part)

    #context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    #SSL connection only working on Python 3+
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    if isTls:
        smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail("dailygenixauto@gmail.com", "harshdhiman01@gmail.com,msdhamija@yahoo.co.in", msg.as_string())
    smtp.quit()
