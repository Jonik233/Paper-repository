from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles
from .forms import ArticleForm
from django.db.models import Max
from django.http import HttpResponseNotFound


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


def submit(request):
    error = ''
    article_id = None

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            article_id = article.id
            return redirect('home')
        else:
            error = 'Form is incorrect'

    form = ArticleForm()
    data = {"form": form, "error": error, "article_id": article_id}

    return render(request, 'main/submit.html', data)



def get_rates_by_criteria(request, field, sort_by):
    if sort_by == 'score':
        articles = Articles.objects.filter(field=field).order_by('-rating_points')
        template = 'main/score_rates.html'
    elif sort_by == 'date':
        articles = Articles.objects.filter(field=field).order_by('-publication_date')
        template = 'main/date_rates.html'
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(request, template, {'articles': articles})


def get_article_by_id(request, id):
    article = get_object_or_404(Articles, id=id)
    return render(request, 'main/paper.html', {'article': article})