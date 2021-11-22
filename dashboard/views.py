from django.shortcuts import render

# Create your views here.

# View for index page. 
def homepage(request):
  return render(request, 'core/homepage.html')