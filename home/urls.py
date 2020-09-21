from django.urls import path
from .views import home, HomePageView, MyView
from django.views.generic.base import TemplateView



urlpatterns = [
    path('', home, name="home"),
    path('home2', TemplateView.as_view(template_name='home2.html')),
    path('home3', HomePageView.as_view(template_name='home3.html')),
    path('view', MyView.as_view()),

]
