from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    
        return render(request, "blog_samples/index.html")
    



def post(request):
    if request.user.is_authenticated:
        return render(request, "blog_samples/post.html")
    else :
        return redirect("my_accounts:login")


def contact(request): 
    return render(request, "blog_samples/contact.html")