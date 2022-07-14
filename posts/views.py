from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def home(request):
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
    
