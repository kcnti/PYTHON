import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('email.html').read_text())
email = EmailMessage()
email['from'] = 'Kikuanone A'
email['to'] = 'kantinun99998@gmail.com'
email['subject'] = 'Hello, Unknown'

email.set_content(html.substitute({'name': 'Earth'}),'html') #format dollar sign

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('kikuanone4321@gmail.com', 'kikuanone1234')
	smtp.send_message(email)
	print('Done')