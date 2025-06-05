from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('competences/', views.competences, name='competences'),
    path('projets/', views.projets, name='projets'),
    path('contact/', views.contact, name='contact'),
]
