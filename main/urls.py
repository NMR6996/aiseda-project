from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("home", views.index, name="home"),
    path("about", views.about, name="about"),
    path("team", views.team, name="team"),
    path("contact-us", views.contact_us, name="contact-us")
]
