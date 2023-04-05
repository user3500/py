import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Leonardo M'
email['to'] = 'leonardmejia817@gmail.com'
email['subject'] = 'you win'

email.set_content(html.substitute(name='tintin'),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('subliminalbiscuit@gmail.com','zlxgchercoiiigku')
    smtp.send_message(email)
    print('all g')
