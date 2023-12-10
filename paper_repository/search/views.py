from django.shortcuts import render
from main.models import Articles

def search(request):
    return render(request, 'search\search.html')

def search_results(request):
    query = request.GET.get('query', '')
    selected_field = request.GET.get('selected_field', '')
    articles = Articles.objects.none()

    if query:
        if selected_field:
            field_value = next((field[0] for field in Articles.CATEGORY_CHOICES if field[1] == selected_field), None)
            if field_value:
                articles = Articles.objects.filter(title__icontains=query, field=field_value)
            else:
                articles = Articles.objects.filter(title__icontains=query)
        else:
            articles = Articles.objects.filter(title__icontains=query)
    
    return render(request, 'search/papers.html', {"articles": articles})