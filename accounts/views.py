from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def after_login(request):
    return render(request,'accounts/after.html')
    # return HttpResponse('this is the page you see when ypu have logged in')

def sign_up_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Success, you have created a user')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/sign_up.html',context)