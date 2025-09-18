from django.contrib import admin
from .models import Home, Customer, Agent


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('price', 'sity', 'location')
    list_filter = ('price', 'sity', 'location')
    search_fields = ('price', 'sity', 'location')
    ordering = ('price',)
    list_display_links = ('price',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name',  'job')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'job')