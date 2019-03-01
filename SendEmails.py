from Session1.settings import SENDER_USERNAME, SENDER_PASSWORD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

recipient_email = 'email@domain.com'

msg = MIMEMultipart()
msg['From'] = SENDER_USERNAME
msg['To'] = recipient_email
msg['Subject'] = 'subject'

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body, 'plain'))

filename = 'PATH_TO_FILE'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(SENDER_USERNAME, SENDER_PASSWORD)

server.sendmail(SENDER_USERNAME, recipient_email, text)
server.quit()
