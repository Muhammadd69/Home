from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Home, Customer, Agent


class HomePageView(TemplateView):
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
