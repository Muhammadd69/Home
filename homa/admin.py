from django.contrib import admin
from .models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('price', 'sity', 'location')
    list_filter = ('price', 'sity', 'location')
    search_fields = ('price', 'sity', 'location')
    ordering = ('price',)
    list_display_links = ('price',)
