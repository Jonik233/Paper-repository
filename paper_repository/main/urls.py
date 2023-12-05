from django.urls import path
from . import views
import registration.views
import search.views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', registration.views.registration, name='registration'),
    path('login/', registration.views.login, name='login'),
    path('search/', search.views.search, name='search'),
    path('rates/', views.rates, name='rates'),
    path('rates/<str:field>/', views.rates_by_score, name='rates_by_score')
]