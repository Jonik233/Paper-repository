from django.urls import path
from . import views
import registration.views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', registration.views.registration, name='registration')
]