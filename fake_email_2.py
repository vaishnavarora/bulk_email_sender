# NOTICE

#Don't change the values as it may lead the code to stop working or running

import smtplib 
from email.message import EmailMessage 
import pwinput
import random 
to_email_i_d = input("enter the email id you want to send email without @gmail.com : "); a = 'vaishgaba@gmail.com'
to_email_id = to_email_i_d + "@gmail.com"
enter = pwinput.pwinput('enter your password : ') 
email = EmailMessage() 
email['from'] = '' # name of person who is sending 
email['to'] = to_email_id, a
email['subject'] = '' #subject of the email 
email.set_content(f"This fake email project is made by Mr. Vaishnav Arora. Please give him credit if your are copying this project")
with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp: 
	smtp.ehlo()
	smtp.starttls() 
	smtp.login('your email id',enter) #enter your email id here 
	smtp.send_message(email)
	print('sent successfully')
