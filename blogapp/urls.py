from django.urls import path
from . import views
from .views import PostDetailView,PostCreateView,PostUpdateView,HomeView,PostDeleteView
urlpatterns = [
    path("",HomeView.as_view(),name='blog-home'),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="update"),
    path("post/create/new",PostCreateView.as_view(),name='create'),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="delete"),

]
