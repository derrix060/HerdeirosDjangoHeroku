from django.contrib import admin
from .models import DonateItem, Evento


class EventoAdmin(admin.ModelAdmin):
    # Showed on details
    fieldsets = [
        (None,  {'fields': ['titulo_text', 'date_date',
                            'local_text', 'description_text',
                            'image_src_text']}),
    ]

    list_display = ('titulo_text', 'date_date', 'local_text')
    list_filter = ['date_date']
    search_fields = ['titulo_text']


class DonateItemAdmin(admin.ModelAdmin):
    # Showed on details
    fieldsets = [
        (None,  {'fields': ['name_text', 'amount',
                            'image_src_text']}),
    ]
    list_display = ('name_text', 'amount')
    list_filter = ['amount']
    search_fields = ['name_text']


# Register your models here.
admin.site.register(DonateItem, DonateItemAdmin)
admin.site.register(Evento, EventoAdmin)
