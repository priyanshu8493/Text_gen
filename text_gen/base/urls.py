from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="Home"),
    path('generate_text/', views.generate_text, name = "generate"),
]