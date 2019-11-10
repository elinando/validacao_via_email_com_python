
import smtplib
from email.mime.text import MIMEText


#gerando 4 numeros aleatorios e cocatenando como string
from random import randint

a=str((randint(0,9)))
b=str((randint(0,9)))
c=str((randint(0,9)))
d=str((randint(0,9)))
x=a+b+c+d

 

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
#  email e senha para logar no servidor
username = 'eaf.alertas@gmail.com'
password = '********'

from_addr = 'eaf.alertas@gmail.com'
#capturando nome do usuario
print('informe seu nome')
nome = str(input())
#capturando email do usuario
print('informe seu email')
destinatario = str(input())
to_addrs = [destinatario]

# neste caso usaremos MIMEText para enviar
# somente texto
message = MIMEText('Olá, '+nome+', seu codigo de verificação é '+x)
message['subject'] = 'CODIGO DE VERIFICAÇÃO - '+x+' - NÃO RESPONDA'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)



# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()

#validando codigo recebido
print('informe o código recebido o seu email:')
y= str(input())

if x == y:
    resp=1
    print('o código é valido')
else:
    resp=0
    print('codigo incorreto')
