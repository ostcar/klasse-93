from django.db import models

class Teilnehmer(models.Model):
    STATE = (
        (0, 'Unbekannt'),
        (1, 'Kommt sicher'),
        (2, 'Kommt nicht'),
        (3, 'Kommt vermutlich'),
        (4, 'Unentschlossen'),
    )
    name = models.CharField(max_length=255)
    mail = models.EmailField(null=True, blank=True)
    comment = models.TextField(blank=True)
    state = models.IntegerField(choices=STATE, default=0, verbose_name="Kommt")

    class Meta:
        ordering  = ("name", )

    def __str__(self):
        return self.name

    def has_mail(self):
        return bool(self.mail)
    has_mail.short_description = 'E-Mail bekannt'
