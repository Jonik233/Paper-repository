from . import views
import search.views
import registration.views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', registration.views.registration, name='registration'),
    path('login/', registration.views.login, name='login'),
    path('logout/', views.home, name='logout'),
    path('search/', search.views.search, name='search'),
    path('logout-current-user/', views.logout_current_user, name='logout_current_user'),
    path('submit/', views.submit, name='submit'),
    path('search_results/', search.views.search_results, name='search_results'),
    path('rates/', views.rates, name='rates'),
    path('rates/<str:field>/<str:sort_by>/', views.get_rates_by_criteria, name='rates_by_criteria'),
    path('article/<int:id>/', views.get_article_by_id, name='article')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)