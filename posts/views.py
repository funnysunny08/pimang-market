from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def home(request):
    query = request.GET.get('query', None) # query 안에 암것도 없으면 None
    min = request.GET.get('min_price', None)
    max = request.GET.get('max_price', None)
    print("min and max: ",min,max)
    if query:
        posts = Post.objects.filter(region__contains=query)
    elif min and max:
        # posts = Post.objects.filter(price__gt=min, price__lt=max)
        posts = Post.objects.filter(price__range=(min,max))
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
        req_photo = request.FILES["photo"]

        Post.objects.create(title=title, user=user, region=region, price=price, content=content, photo=req_photo)
        return redirect("/")

    context = {}

    return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    # 정참조 부모 <- 자식
    user_name = post.user.name
    user_age = post.user.age

    # 역참조 부모 -> 자식
    user = post.user
    # all_post = user.post_set.all()
    all_post = user.post_user.all()

    context = {
        "post":post,
        "user_name":user_name,
        "user_age":user_age,
        "all_post":all_post
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