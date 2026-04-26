from django.shortcuts import render

def site_home(request):
    return render(request, 'site/home.html')
