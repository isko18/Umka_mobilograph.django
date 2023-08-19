from django.shortcuts import render
from .models import About
from apps.homepage.models import Umka


def about(request):
    about = About.objects.latest("id")
    umka = Umka.objects.latest("id")
    context = {
        "about" : about,
        "umka" : umka
        
    }
    return render(request, "about-me.html", context)
