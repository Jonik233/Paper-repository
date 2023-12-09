from django.shortcuts import render
from main.models import Articles

def search(request):
    return render(request, 'search\search.html')

def search_results(request):
    query = request.GET.get('query', '')
    if query:
        articles = Articles.objects.filter(title__icontains=query)
    else:
        articles = Articles.objects.none()
    
    return render(request, 'search\papers.html', {"articles":articles})