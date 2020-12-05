from django.urls import path
from . import views 
from .views import (
    EventListView,
    EventDetailView
)

urlpatterns = [
    path('',views.index,name="home"),
    path('test/',views.test,name="test"),
    path('gallery/',views.gallery,name="gallery"),
    path('about/',views.about,name="about"),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('details/<int:pk>/',views.EventDetailView.as_view(),name="event-details"),
    path('event/',views.EventListView.as_view(),name="event"),
    path('booking/',views.booking,name="booking"),
    path('about/',views.about,name="about"),
    path('404/',views.error,name="404-error"),
]