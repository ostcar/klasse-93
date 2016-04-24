from django.shortcuts import render
from django.views.generic import ListView

from .models import Teilnehmer

class HomeView(ListView):
    model = Teilnehmer
    template_name ="app/index.html"
