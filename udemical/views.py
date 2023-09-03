from django.shortcuts import render,HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request,'home/index.html' )
def about(request):
    return render (request,'about/about.html')
def contact(request):
    return render(request,'contact/contact.html')



