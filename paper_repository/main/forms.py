from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateInput, FileInput, Select

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'field', 'authors', 'content', 'publication_date', 'pdf_file']
        
        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title'
            }),
            
            'field': Select(choices=Articles.CATEGORY_CHOICES, attrs={"class":'form-control'}),
            
            'authors': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter authors'
            }),
            
            'content': Textarea(attrs={
                'class':'form-control',
                'rows':5,
                'placeholder':'Enter abstract'
            }),
            
            'publication_date': DateInput(attrs={
                'class':'form-control',
                'type':'date'
            }),
            
            'pdf_file': FileInput(attrs={
                'class':'form-control-file',
                'accept': '.pdf'
            })
        }