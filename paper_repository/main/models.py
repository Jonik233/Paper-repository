from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=500)
    author = models.CharField('Author', max_length=255)
    content = models.TextField('Content')
    rating_points = models.IntegerField()
    
    CATEGORY_CHOICES = [
        ("physics", "Physics"), 
        ("chemistry", "Chemistry"),
        ("economics", "Economics"),
        ("history", "History"),
        ("math", "Math"),
        ("biology", "Biology"),
        ("machine learning", "Machine Learning")
    ]
    field = models.CharField('Field', max_length=100, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.title