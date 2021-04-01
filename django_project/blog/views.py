from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
posts = [
   {
       'author':'Coreyms',
       'title':'Blog posts',
       'content':'First post content',
       'date_posted':'August 27, 2018'
   },
    {
       'author':'naresh',
       'title':'Blog posts 2',
       'content':'second post content',
       'date_posted':'August 28, 2018'
   }

]
##this will handle the traffic from homepage
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html')
# def about(request):
    # return HttpResponse('<h1> Blog About</h1>')