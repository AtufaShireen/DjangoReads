from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.



def home(request):

    content={'posts':Post.objects.all()}
    return render(request, 'blogapp/home.html',content)


def about(request):
    return render(request, 'blogapp/about.html',{'title':'About'})


def posts(request):
    return HttpResponse('<h1>All posts here..</h1>')


def post(request):
    return HttpResponse('<h1>A  detailed post..</h1>')


def update(request):
    return HttpResponse('<h1>Update your post..</h1>')


def delete(request):
    return HttpResponse('<h1>Delete a post..</h1>')
