from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post

# Create your views here.





def index(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    
    return render(request,"blog/index.html",{
        "posts": latest_posts
    })

def post(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request,"blog/allpost.html",{
        "all_posts":all_posts
    })

def post_detail(request,slug):

    identified_post = get_object_or_404(Post,slug=slug)
    return render(request,"blog/postdetail.html",{
        "post": identified_post
    })