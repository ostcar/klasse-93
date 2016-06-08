from django.core.mail import send_mail
from django.template.loader import get_template

from .models import Teilnehmer

def send_mail1():
    mail_template = get_template('mail/mail1.tpl')
    for teilnehmer in Teilnehmer.objects.exclude(mail='').exclude(mail=None):
        body = mail_template.render({'teilnehmer': teilnehmer})
        send_mail(
            'Klassenbuch und Bilder',
            body,
            'info@klasse-93.de',
            [teilnehmer.mail],
            fail_silently=False)

def send_mail2():
    mail_template = get_template('mail/mail2.tpl')
    for teilnehmer in Teilnehmer.objects.exclude(mail='').exclude(mail=None):
        body = mail_template.render({'teilnehmer': teilnehmer})
        send_mail(
            'Klassentreffen letzte Erinnerung',
            body,
            'info@klasse-93.de',
            [teilnehmer.mail],
            fail_silently=False)
