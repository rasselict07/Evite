from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EventSignUp.as_view(), name='event_signup'),
    path('event_subscribe/', views.eventsubscribe, name='event_subscribe'),
    path('event_unsubscribe/', views.eventunsubscribe, name='event_unsubscribe'),
]
