from django.urls import path
from .views import portfolio,project_1,project_video

urlpatterns = [
    path('portfolio/', portfolio, name="portfolio"),
    path('project-1/<int:id>/', project_1, name="project-1"),
    path('project-video/<int:id>/', project_video, name="project-video"),


]