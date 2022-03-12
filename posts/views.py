import re
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm,UpdatePostForm
from .models import Post,Comment
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def posts_view(request):
    if 'query' in request.GET:
        query = request.GET['query']
        all_Posts = Post.objects.filter(title__icontains=query)
    else:
        all_Posts = Post.objects.all().order_by('-date')

    page_num = request.GET.get('page', 1)
    paginator = Paginator(all_Posts, 6) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)


    return render(request,'posts/posts.html',{'posts':page_obj})

@login_required
def create_posts_view(request):
    form = CreatePostForm(request.POST or None)
    if form.is_valid():
        author = form.save(commit=False)
        author.author = request.user
        author.save()
        messages.success(request,'Success, you have created a post')

        return redirect('posts')
    return render(request,'posts/create_post.html',{'form': form})
    
@login_required
def detail_view(request,id):
    post = Post.objects.get(id=id)
    
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        messages.success(request,'Success, you made a comment')

        return redirect('details', id=post.id)    
    return render(request,'posts/detail.html',{'form':form,'post':post})


def update_post_view(request,id):
    # post = get_object_or_404(Post,id=id)
    post = Post.objects.get(id=id)
    form = UpdatePostForm(request.POST or None,instance = post)
    if form.is_valid():
        form.save()
        messages.success(request,'Success, you have updated the post')
        return redirect('details',id=id)
    return render(request,'posts/update_post.html',{'form':form,'post':post})

def delete_view(request, id):
    # data = get_object_or_404(Post,id=id)
    post = Post.objects.get(id=id)
    if request.method =="POST":
        post.delete()
        # data.delete()
        # after deleting redirect to
        # home page
        messages.success(request,'Success, you have deleted the post')

        return redirect('posts')
    return render(request, 'posts/delete.html',{'post':post})

def delete_comment_view(request, id):
    # data = get_object_or_404(Post,id=id)
    comment = Comment.objects.get(id=id)
    if request.method =="POST":
        comment.delete()
        # data.delete()
        # after deleting redirect to
        # home page
        messages.success(request,'Success, you have deleted your comment')

        return redirect('posts')
    return render(request, 'posts/delete_comment.html',{'comment':comment})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            messages.success(request,'Thank you for your message. We will get back to you as soon as possible.')

            return redirect('posts')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')