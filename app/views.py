from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Teilnehmer, Comment

class HomeView(ListView):
    model = Teilnehmer
    template_name ="app/index.html"

    def get_context_data(self, **context):
        teilnehmer_count = sum(
            1
            for object in self.object_list
            if object.state in (
                Teilnehmer.STATE_PROPABLY, Teilnehmer.STATE_SURE))

        comment_list = Comment.objects.all()

        return super().get_context_data(
            teilnehmer_count=teilnehmer_count,
            comment_list=comment_list,
            **context)

class CommentCreateView(CreateView):
    model = Comment
    fields = ('author', 'text')
    success_url = '/'
