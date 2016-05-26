from django.db import models
from django.contrib.postgres.fields import ArrayField
import random
import string
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def create_token(length=8):
    while True:
        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
        if not Teilnehmer.objects.filter(token=token).exists():
            return token

class Teilnehmer(models.Model):
    STATE_UNKNOWN = 0
    STATE_SURE = 1
    STATE_NOT = 2
    STATE_PROPABLY = 3
    STATE_UNDESIDED = 4
    STATE = (
        (STATE_UNKNOWN, 'Unbekannt'),
        (STATE_SURE, 'Kommt sicher'),
        (STATE_NOT, 'Kommt nicht'),
        (STATE_PROPABLY, 'Kommt vermutlich'),
        (STATE_UNDESIDED, 'Unentschlossen'),
    )

    name = models.CharField(max_length=255)
    mail = models.EmailField(null=True, blank=True)
    intern_comment = models.TextField(blank=True, verbose_name="Kommentar")
    state = models.IntegerField(
        choices=STATE,
        default=0,
        verbose_name="Ist dabei",
        help_text="Wird am Klassentreffen dabei sein.")

    token = models.CharField(
        max_length=32,
        null=True,
        unique=True)

    mail_public = models.BooleanField(
        default=True,
        verbose_name="E-Mail Adresse darf veröffentlicht werden",
        help_text="Die Adresse wird nur Klassenintern veröffentlicht.")
    location_current = models.CharField(
        max_length=255,
        verbose_name="Wohnort",
        blank=True)
    job = models.CharField(
        max_length=255,
        verbose_name="Beruf/Beschäftigung",
        blank=True)
    relationship_status = models.CharField(
        max_length=32,
        verbose_name="Beziehungsstatus",
        default="Zu haben")
    kids = models.PositiveIntegerField(
        default=0,
        verbose_name="Anzahl Kinder")
    image_new = ProcessedImageField(
        upload_to='teilnehmer',
        verbose_name="Aktuelles Bild",
        null=True,
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 99})
    image_old = ProcessedImageField(
        upload_to='teilnehmer',
        verbose_name="Erstes klassenbild",
        null=True,
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 99})
    locations_old = ArrayField(
        models.CharField(max_length=255),
        verbose_name="Wohnorte seit der Schulzeit",
        default=list,
        blank=True,
        help_text="Durch ein Komma getrennt")
    hobbies = ArrayField(
        models.CharField(max_length=255),
        verbose_name="hobbies",
        default=list,
        help_text="Durch ein Komma getrennt")
    school_memory = models.TextField(
        verbose_name="Erinnerung an Schulzeit",
        help_text="Eine besondere Erinnerung an die gemeinsame Schulzeit.",
        blank=True)

    class Meta:
        ordering  = ("name", )

    def __str__(self):
        return self.name

    def has_mail(self):
        return bool(self.mail)
    has_mail.short_description = 'E-Mail bekannt'

    def get_token(self):
        if not self.token:
            self.token = create_token()
            self.save()
        return self.token

    def get_edit_link(self):
        return "{host}{path}".format(
            host="http://klasse-93.de",
            #host="localhost:8000",
            path=reverse("edit", kwargs={'token': self.get_token()}),
        )

    def send_token(self):
        send_mail(
            'Klassenbuch',
            """Hallo {name},

hier ist dein persönlicher Link:

{link}

Viele Grüße
das Klassentreffenteam""".format(
                name=self.name,
                link=self.get_edit_link()
            ),
            'info@klasse-93.de',
    [self.mail], fail_silently=False)


class Comment(models.Model):
    teilnehmer = models.ForeignKey(Teilnehmer)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date", )

    def __str__(self):
        return (self.text[:30] + '...') if len(self.text) > 30 else self.text
