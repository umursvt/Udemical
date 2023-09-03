from django.forms import ModelForm 
from .models import Article
from django import forms
from ckeditor.widgets import CKEditorWidget

class ArticleForm(ModelForm):
    content = forms.CharField(max_length=1000,widget=CKEditorWidget() )
    class Meta:
        model=Article
        fields= ['title','content']