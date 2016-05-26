from django import forms
from .models import Comment, Teilnehmer


class CleanMailMixin:
    def clean_mail(self):
        mail = self.cleaned_data['mail']
        try:
            teilnehmer = Teilnehmer.objects.filter(mail__iexact=mail).get()
        except:
            raise forms.ValidationError(
                "Die E-Mail-Adresse ist unbekannt, bitte schreibe eine E-Mail "
                "an info@klasse-93.de um deine E-Mail-Adresse freizuschalten")
        self.cleaned_data['teilnehmer'] = teilnehmer
        return mail


class CommentForm(CleanMailMixin, forms.ModelForm):
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


class SendTokenForm(CleanMailMixin, forms.Form):
    mail = forms.EmailField(label="E-Mail-Adresse")


class TeilnehmerForm(forms.ModelForm):
    class Meta:
        model = Teilnehmer
        fields = [
                'state',
                'location_current',
                'job',
                'relationship_status',
                'kids',
                'image_new',
                'image_old',
                'locations_old',
                'hobbies',
                'school_memory',
            ]
