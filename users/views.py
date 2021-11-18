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
    return render(request, '/home/cosmina/Reporting/users/templates/registration.html', {'form': form})