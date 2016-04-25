from django.shortcuts import render
from django.views.generic import ListView

from .models import Teilnehmer

class HomeView(ListView):
    model = Teilnehmer
    template_name ="app/index.html"

    def get_context_data(self, *context):
        return super().get_context_data(teilnehmer_count=sum(1 for object in self.object_list if object.state in (Teilnehmer.STATE_PROPABLY, Teilnehmer.STATE_SURE)))
