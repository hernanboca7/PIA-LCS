#
# LPCS - Practica 12 (3.2 - Envío de correos)
# Alumno: Hernán Bocanegra García 
# Matricula: 1851986
#
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "hernanbg01@gmail.com"
receiver_email = "gerardo.bernal@uanl.edu.mx"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Prueba de envio (Script Python) - 1851986"
message["From"] = sender_email
message["To"] = receiver_email

# Crear el texto plano y la versión de HTML para tu mensaje
text = """\
Practica 12
Ejercicio de la practica 12 para envío de correos
Alumno: Hernan Bocanegra Garcia
Matricula: 1851986"""
html = """\
<html>
<head>
</head>
<body>
    <img src="https://plataformanexus.uanl.mx/Contenedores%20L%2FContenedor_7804%2F2696_06-09-2023_08-18-33_1568190351.png" width="232" height="199">

    <h2>Practica 12</h2>

	<p>Ejercicio de la practica 12 para envío de correos</p>
	<p> <b> Alumno: </b> Hernan Bocanegra Garcia</p>
    <b> Matricula: </b> 1851986
</body>
</html>
"""

# Convertirlos en objectos plano/html MIMEText 
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Agregar partes HTML/texto sin formato al mensaje MIMEMultipart
# El cliente de correo electrónico intentará mostrar primero la última parte
message.attach(part1)
message.attach(part2)

# Cree una conexión segura con el servidor y envíe un correo electrónico
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )