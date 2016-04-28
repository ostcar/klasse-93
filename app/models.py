from django.db import models

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
    comment = models.TextField(blank=True)
    state = models.IntegerField(choices=STATE, default=0, verbose_name="Kommt")
    is_teacher = models.BooleanField(default=False, verbose_name="Ist Lehrer")

    class Meta:
        ordering  = ("name", )

    def __str__(self):
        return self.name

    def has_mail(self):
        return bool(self.mail)
    has_mail.short_description = 'E-Mail bekannt'


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date", )

    def __str__(self):
        return (self.text[:30] + '...') if len(self.text) > 30 else self.text
