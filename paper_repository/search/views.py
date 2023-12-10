from django.shortcuts import render
from main.models import Articles

def search(request):
    return render(request, 'search\search.html')

def search_results(request):
    query = request.GET.get('query', '')
    author = request.GET.get('author', '')
    selected_field = request.GET.get('selected_field', '')
    articles = Articles.objects.none()

    if query:
        query_conditions = {"title__icontains":query}
        
        if selected_field:
            field_value = next((field[0] for field in Articles.CATEGORY_CHOICES if field[1] == selected_field), None)
            if field_value:
                query_conditions["field"] = field_value
        
        if author:
            query_conditions["authors__icontains"] = author
        
        articles = Articles.objects.filter(**query_conditions)
    return render(request, 'search/papers.html', {"articles": articles})