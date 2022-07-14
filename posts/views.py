from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def home(request):
    query = request.GET.get('query', None) # query 안에 암것도 없으면 None
    if query:
        posts = Post.objects.filter(region__contains=query)
    else:
        posts = Post.objects.all()

    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        user = request.POST["user"]
        region = request.POST["region"]
        price = request.POST["price"]
        content = request.POST["content"]

        Post.objects.create(title=title, user=user, region=region, price=price, content=content)
        return redirect("/")

    context = {}

    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/detail.html", context=context)
    
def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        user = request.POST["user"]
        region = request.POST["region"]
        price = request.POST["price"]
        content = request.POST["content"]

        Post.objects.filter(id=id).update(title=title, user=user, region=region, price=price, content=content)
        return redirect(f"/post/{id}")
    
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request, template_name="posts/update.html", context=context)

def delete(request, id):
    #if request.method == "POST":
    Post.objects.filter(id=id).delete()
    return redirect("/")