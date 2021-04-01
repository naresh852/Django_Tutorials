from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
##this will handle the traffic from homepage
def home(request):
    return render(request,'blog/home.html')
def about(request):
    return HttpResponse('<h1> Blog About</h1>')