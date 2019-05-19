from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    post_list = Post.objects.all()
    if request.user.is_authenticated:
        my_liked_post = Post.objects.filter(user = request.user)
    else:
        my_liked_post = None
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs,
                                        'liked_post':my_liked_post
                                        }
                                        )

def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments_list = Comment.objects.filter(post = post_id)
    return render(request, 'detail.html', {'post':post, 'comments':comments_list})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Post()
    new_post.title=request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.datetime.now()
    new_post.save()
    return redirect('home')

def edit(request, post_id):
    edit_post = Post.objects.get(id=post_id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request, post_id):
    update_post = Post.objects.get(id=post_id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('home')

def delete(request, post_id):
    delete_post=Post.objects.get(id=post_id)
    delete_post.delete()
    return redirect('home')

def new_comment(request, post_id):
    comment = Comment()
    comment.writer = request.POST['writer']
    comment.content = request.POST['content']
    comment.post = get_object_or_404(Post, pk=post_id)
    comment.save()
    return redirect('detail', post_id)

def like(request,post_id):
    post=get_object_or_404(Post, pk = post_id)
    if post.user.filter(username=request.user.username).exists():
        post.user.remove(request.user)    
    else:
        post.user.add(request.user)
    post.save()
    return redirect('detail', post_id)