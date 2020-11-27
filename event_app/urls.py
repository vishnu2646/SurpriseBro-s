from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('gallery/',views.gallery,name="gallery"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('details/',views.details,name="details"),
    path('event/',views.event,name="event"),
    path('booking/',views.booking,name="booking"),
    path('404/',views.error,name="404-error"),
]