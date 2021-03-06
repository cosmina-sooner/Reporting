from django.shortcuts import render
from .forms import UserRegisterForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# from django.urls import reverse

#forms
def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        # return HttpResponseRedirect(reverse('homepage'))
            
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')  
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'dashboard/homepage.html')