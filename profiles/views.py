from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import update_user_form
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from posts.models import Post,Comment
from .forms import update_user_form,update_profile_form

@login_required
def profile_view(request):
    posts = Post.objects.filter(author=request.user)
    post_count = posts.count()
    comments = Comment.objects.filter(user=request.user)
    comments_count = comments.count()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page1')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    paginator = Paginator(comments, 6)
    page = request.GET.get('page2')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request,'profiles/profiles.html',{'post_count': post_count,'posts':posts,'comments_count':comments_count,'comments': comments})

@login_required
def profile_update_view(request):
    if request.method == "POST":
        updateUserForm = update_user_form(request.POST or None, instance=request.user)
        updateProfileForm = update_profile_form(request.POST or None, request.FILES or None, instance=request.user.profile)
        if updateUserForm.is_valid() and updateProfileForm.is_valid():
            updateUserForm.save()
            updateProfileForm.save()
            messages.success(request,'Success, you have updated your profile')
            return redirect('profile')
    else:
        updateUserForm = update_user_form(instance=request.user)
        updateProfileForm = update_profile_form(instance=request.user.profile)
     
    context = {
        'updateUserForm': updateUserForm,
        'updateProfileForm': updateProfileForm,
    }
    return render(request,'profiles/profile_update.html',context)

