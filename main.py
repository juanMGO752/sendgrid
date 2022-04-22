import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from jinja2 import Environment, FileSystemLoader

# jinja2 asignacion de carpeta templates y uso de un template html

fileLoader = FileSystemLoader("templates")
env = Environment(loader = fileLoader)
rendered = env.get_template("gallery.html").render(title="HOLA MUNDO")

# sendgrid envio de correo 

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("juangonzaoso@gmail.com")  # Correo verificado en sendgrid
# to_email = To("jmgonzalez81223@umanizales.edu.co")  # Change to your recipient
to_email= ["jmgonzalez81223@umanizales.edu.co","juangonzaoso@gmail.com"] # lista de correos a enviar
subject = "mensaje automatico" #Asunto
content = Content("text/html", rendered) # (text/html) / (text/plain)

mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)

print("/////////")
print(response.status_code)
print("/////////")
print(response.headers)
print("/////////")
print(response.body)
print("/////////")

