from django.shortcuts import render
from . models import Umka, Social_network
from apps.portfolio.models import Portfolio


# Create your views here.
def index(request):
    umka = Umka.objects.latest("id")
    portfolio = Portfolio.objects.all()

    social_network = Social_network.objects.latest("id")
    context = {
        'umka' : umka,
        'social_network' : social_network,
        'portfolio' : portfolio
    }
    return render(request,'index.html',context)


