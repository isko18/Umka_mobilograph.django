from django.shortcuts import render
from .models import Portfolio, Project_video
from apps.homepage.models import Umka



# Create your views here.

def portfolio(request):
    portfolio = Portfolio.objects.all()
    project_video = Project_video.objects.all()
    umka = Umka.objects.latest("id")
    context = {
        'portfolio' : portfolio,
        'umka' : umka,
        'project_video' : project_video 
    }
    return render(request, "portfolio.html", context)


def project_1(request, id):
    portfolio = Portfolio.objects.get(id=id)
    umka = Umka.objects.latest("id")
    context = {
        'portfolio' : portfolio,
        'umka' : umka,


    }
    return render(request,'project-1.html',context) 



def project_video(request, id):
    portfolio = Portfolio.objects.all()
    project_video = Project_video.objects.get(id=id)
    context = {
        'portfolio' : portfolio,
        'project_video' : project_video 

    }
    return render(request,'project-video.html',context) 