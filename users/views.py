from django.shortcuts import render
from .forms import UserRegisterForm

#forms
def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
           
    else:
        form = UserRegisterForm()
    return render(request, 'core/registration.html', {'form': form})