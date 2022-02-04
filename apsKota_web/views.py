from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, "home.html")

def post(request):
    post = Post.objects.all()
    return render(request, "post.html", {'posts': post})

def post_detail(request, slug):
    context = {}
    try: 
        post_obj =  Post.objects.filter(slug = slug).first()
        context["post_obj"] = post_obj
    except Exception as e :
        print(e)
    return render(request, "post_detail.html", context)

def post_detail(request, slug):
    post = Post.objects.get(slug =slug)
    return render(request, "post_detail.html", {"post": post})
