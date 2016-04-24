from django.contrib import admin
from django.db.models import Q

from .models import Teilnehmer


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


@admin.register(Teilnehmer)
class  TeilnehmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'state')
    list_filter = (HasMailFilter, 'state')
