from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    posts = [
        {
            'author': 'Atufa Shireen',
            'title': 'Making A Web App',
            'subtitle': 'Is making webapp difficult than website',
            'story': 'A web app, is an application that runs online, has usually quite a bit'
                     ' of functionality and does a bunch of data crunching on the back-end. So it is typical',
            'published': 'April 14 2002'
        },
        {
            'author': 'John Doe',
            'title': 'Making A Website',
            'subtitle': 'How to make a cms website',
            'story': 'Building a content management system can seem like a daunting task to the novice PHP developer.'
                     ' However, it needn’t be that difficult.In this tutorial I’ll show you how to build a basic, but fully functional',
            'published': 'April 20 2002'
        }

    ]
    content={'posts':posts}
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
