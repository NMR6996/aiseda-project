from django.shortcuts import render
from .models import Team


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def team(request):
    teams = Team.objects.all()
    return render(request, "team.html", {"teams": teams})


def contact_us(request):
    return render(request, "contact-us.html")
