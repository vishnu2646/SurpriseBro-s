from django.urls import path
from . import views 
from .views import (
    EventListView,
    EventDetailView,
    IndexView
)

urlpatterns = [
    path('',views.IndexView.as_view(),name="home"),
    path('test/',views.test,name="test"),
    path('gallery/',views.gallery,name="gallery"),
    path('about/',views.about,name="about"),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('details/<int:pk>/',views.EventDetailView.as_view(),name="event-details"),
    path('event/',views.EventListView.as_view(),name="event"),
    path('franchise/',views.franchise,name="franchise"),
    path('refund/',views.refund,name="refund"),
    path('about/',views.about,name="about"),
    path('search/',views.search,name="search"),
    path('404/',views.error,name="404-error"),
]