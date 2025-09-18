from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Home


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        homes = Home.objects.all()
        context = {
            'homes': homes,
        }
        return render(request, 'index.html', context)
