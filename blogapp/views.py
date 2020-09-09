from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blogapp/home.html'  # <app>/<model>_<viewtype>.html
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post # blogapp/post_detail.html

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content','bg_pic']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content','bg_pic']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author