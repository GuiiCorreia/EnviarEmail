import smtplib
import ssl
from email.message import EmailMessage

# Define email origem, senha gerada pelo proprio gmail e email de origem
email_sender = 'testar.enviar.email@gmail.com' 
email_password = 'ybxkttqwryhjviuc'
email_receiver = 'smartleadscrawler@gmail.com'

# conteudo do email
subject = 'Teste para titulo do email'
body = """
Teste corpo do email
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Enviar o email em si
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())