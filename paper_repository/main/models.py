from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=500)
    authors = models.CharField('Authors', max_length=500)
    content = models.TextField('Content')
    rating_points = models.IntegerField()
    publication_date = models.DateField(auto_now_add=True)
    
    CATEGORY_CHOICES = [
        ("physics", "Physics"), 
        ("chemistry", "Chemistry"),
        ("economics", "Economics"),
        ("math", "Math"),
        ("biology", "Biology"),
        ("machine learning", "Machine Learning")
    ]
    field = models.CharField('Field', max_length=100, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"