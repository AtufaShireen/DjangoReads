from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="about"),
    path("posts/", views.posts, name="posts"),
    path("post/", views.post, name="post"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),

]
