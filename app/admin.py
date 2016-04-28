from django.contrib import admin
from django.db.models import Q

from .models import Teilnehmer, Comment


class HasMailFilter(admin.SimpleListFilter):
    title = 'E-Mail-Adresse bekannt'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'mail'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('bekannt', 'Bekannt'),
            ('unbekannt', 'Unbekannt'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'bekannt':
            return queryset.exclude(mail="").exclude(mail__isnull=True)
        if self.value() == 'unbekannt':
            return queryset.filter(Q(mail="") | Q(mail__isnull=True))


def set_status_unknown(modeladmin, request, queryset):
    queryset.update(state=Teilnehmer.STATE_UNKNOWN)
set_status_unknown.short_description = "Unbekannt ob er/sie kommt"


def set_status_sure(modeladmin, request, queryset):
    queryset.update(state=Teilnehmer.STATE_SURE)
set_status_sure.short_description = "Kommt sicher"


def set_status_not(modeladmin, request, queryset):
    queryset.update(state=Teilnehmer.STATE_NOT)
set_status_not.short_description = "Kommt nicht"


def set_status_propably(modeladmin, request, queryset):
    queryset.update(state=Teilnehmer.STATE_PROPABLY)
set_status_propably.short_description = "Kommt vermutlich"


def set_status_undesided(modeladmin, request, queryset):
    queryset.update(state=Teilnehmer.STATE_UNDESIDED)
set_status_undesided.short_description = "Unentschieden ob er/sie kommt"


@admin.register(Teilnehmer)
class  TeilnehmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'state', 'is_teacher')
    list_filter = (HasMailFilter, 'state', 'is_teacher')
    preserve_filters = True
    actions = [set_status_unknown, set_status_sure, set_status_not, set_status_propably, set_status_undesided]


@admin.register(Comment)
class  CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', '__str__')
    list_filter = ('author', )
    preserve_filters = True
