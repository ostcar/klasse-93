from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CommentForm, SendTokenForm
from .models import Comment, Teilnehmer


class HomeView(ListView):
    model = Teilnehmer
    template_name = "app/index.html"

    def get(self, request, *args, **kwargs):
        self.token_form = SendTokenForm()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.token_form = SendTokenForm(request.POST)
        if self.token_form.is_valid():
            self.token_form.cleaned_data['teilnehmer'].send_token()

        return super().get(request, *args, **kwargs)

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
            token_form=self.token_form,
            **context)


class CommentCreateView(CreateView):
    model = Comment
    success_url = '/'
    form_class = CommentForm


class TeilnehmerUpdateView(UpdateView):
    model = Teilnehmer
    fields = [
            'state',
            # 'location_current',
            # 'locations_old',
            # 'relationship_status',
            # 'kids',
            # 'image_new',
            # 'image_old',
            # 'job',
            # 'hobbies',
        ]
    slug_url_kwarg = 'token'
    slug_field = 'token'

    def get_success_url(self):
        return reverse("edit", kwargs={'token': self.object.get_token()})


class TeilnehmerDetailView(DetailView):
    model = Teilnehmer
    slug_url_kwarg = slug_field = 'token'


class TeilnehmerListView(ListView):
    queryset = Teilnehmer.objects.exclude(location_current="")
