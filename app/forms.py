from django import forms
from .models import Comment, Teilnehmer


class CommentForm(forms.ModelForm):
    mail = forms.EmailField(label="E-Mail-Adresse", help_text="Die E-Mail-Adresse wird nicht angezeigt. Anhand der E-Mail-Adresse ermitteln wir den Namen, der über deinem Kommentar erscheint.")

    class Meta:
        model = Comment
        fields = ('mail', 'text', )

    def save(self, commit=True):
        instance = super().save(commit=False)
        mail = self.cleaned_data['mail']
        instance.teilnehmer = Teilnehmer.objects.filter(mail__iexact=mail)[0]
        if commit:
            instance.save()
        return instance


    def clean_mail(self):
        mail = self.cleaned_data['mail']
        if not Teilnehmer.objects.filter(mail__iexact=mail).exists():
            raise forms.ValidationError("Die E-Mail-Adresse ist unbekannt, bitte schreibe eine E-Mail an info@klasse-93.de um deine E-Mail-Adresse freizuschalten")
        return mail
