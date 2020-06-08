from django.core.mail import EmailMessage

from django.template.loader import get_template

def contact_send_email(name, email, subject, amessage):
    context = {

    'name': name,

    'email': email,

    'subject': "Form Submission",

    'amessage': amessage,

    }

    cfrom = 'Luketyler.business@gmail.com'

    #pass context to template

    message = get_template('contact-email.html').render(context)

    msg = EmailMessage(subject, message, cfrom, email)

    msg.content_subtype = "html"

    msg.send()