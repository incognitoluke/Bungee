from django.core.mail import EmailMessage

from django.template.loader import get_template

def alert_email(name, email, amessage):
    context = {

    'name': name,

    'email': email,

    'subject': "Form Submission",

    'amessage': amessage,

    }

    cfrom = 'Luketyler.business@gmail.com'
    subject = "Thank you! We've received your donation submission ☑"
    to = [email]
    #pass context to template

    message = get_template('contact-email.html').render(context)

    msg = EmailMessage(subject, message, cfrom, to)

    msg.content_subtype = "html"

    msg.send()