from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from article.form import ArticleForm
from django.contrib import messages

# Create your views here.



def software(request):
    articles = Article.objects.all()
    return render(request, 'software/software.html', {'articles': articles})

def math(request):
    return render(request,'math/math.html')



def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'software/article_detail/article_detail.html', context)

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.iss_valid():
        form.save()
        messages.success(request,'Makale oluşturuldu.')
        return redirect('index')
    content = {
        'form':form
    }
    return render(request,'articles/addArticle.html',content)