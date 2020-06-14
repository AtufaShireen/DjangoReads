from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request=='POST':
        form=UserCreationForm(request.post)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}')
            return redirect('blog-home')
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})