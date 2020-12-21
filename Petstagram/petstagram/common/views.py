from django.shortcuts import render
from django.views import generic as view


class LandingPage(view.TemplateView):
    template_name = 'landing_page.html'
