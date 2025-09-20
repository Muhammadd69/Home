from django.shortcuts import render
from django.views import View
from .models import Home, Customer, Agent


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        homes = Home.objects.all()
        customers = Customer.objects.all()
        agents = Agent.objects.all()
        context = {
            'homes': homes,
            'customers': customers,
            'agents': agents,
        }
        return render(request, 'index.html', context)


class ServiceView(View):
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        context = {
            'customers': customers,
        }
        return render(request, 'services.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        agents = Agent.objects.all()
        context = {
            'agents': agents,
        }
        return render(request, 'about.html', context)


class PropertiesView(View):
    def get(self, request, *args, **kwargs):
        homes = Home.objects.all()
        context = {
            'homes': homes,
        }
        return render(request, 'properties.html', context)
