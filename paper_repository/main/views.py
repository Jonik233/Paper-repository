from django.shortcuts import render
from .models import Articles
from django.db.models import Max

def home(request):
    max_ratings = Articles.objects.values('field').annotate(max_rating=Max('rating_points'))
    
    top_articles = []
    
    for entry in max_ratings:
        top_article = Articles.objects.filter(field=entry['field'], rating_points=entry['max_rating']).first()
        if top_article:
            top_articles.append(top_article)
                       
    return render(request, 'main/home.html', {"articles": top_articles})


def rates(request):
    return render(request, 'main/rates.html')


def rates_by_score(request, field):
    articles = Articles.objects.filter(field=field).order_by('-rating_points')
    return render(request, 'main/score_rates.html', {'articles': articles})