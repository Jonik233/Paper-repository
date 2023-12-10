from django.shortcuts import render
from main.models import Articles

def search(request):
    return render(request, 'search\search.html')

def search_results(request):
    query = request.GET.get('query', '')
    selected_field = request.GET.get('selected_field', '')

    if query:
        if selected_field == "Physics":  
            articles = Articles.objects.filter(title__icontains=query, field='physics')
        elif selected_field == "Math":  
            articles = Articles.objects.filter(title__icontains=query, field='math')
        elif selected_field == "Economics":  
            articles = Articles.objects.filter(title__icontains=query, field='economics')
        elif selected_field == "Chemistry":  
            articles = Articles.objects.filter(title__icontains=query, field='chemistry')
        elif selected_field == "Biology":  
            articles = Articles.objects.filter(title__icontains=query, field='biology')
        elif selected_field == "Machine Learning":  
            articles = Articles.objects.filter(title__icontains=query, field='machine learning')
        else:
            articles = Articles.objects.filter(title__icontains=query)
    else:
        articles = Articles.objects.none()

    return render(request, 'search/papers.html', {"articles": articles})