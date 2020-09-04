import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_add = 'pp099678@gmail.com'
fopen = open('emails.txt','rt')
list_of_emails = fopen.read().split(',')
to_add = list_of_emails
msg = MIMEMultipart()
msg['from'] = from_add
msg['to'] = ",".join(to_add)
msg['subject'] = 'Just for fun'
body = 'Hello world friends, this is just for fun ' \
       'Yes this is your classmate Piyush got your ids from various excel sheets' \
       'Actually I discovered a new python library that collaborates' \
       'with gmail helping us to send mails in few lines of code,so just thought of trying to send ' \
       'my chuddy buddy classmates !!! ' \
       '1 sender 43 receivers 30 lines of code 10 min(did first time) of time , That is the beauty of Python' \
       'Thanks for your time and sorry for inconvenience'
msg.attach(MIMEText(body,'plain'))
email = 'pp099678@gmail.com'
password = 'Piyush4298'
try:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
except:
    print('Not found')
mail.ehlo()
mail.starttls()
mail.login(email, password)
text = msg.as_string()
mail.sendmail(from_add, to_add,text)
mail.quit()
