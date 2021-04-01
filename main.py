# This is a sample Python script.

''' pip install django
pip install django == 2.1.5 # to install a particular version
python -m django --version #to check django version
django-admin help subcommand
django-admin startproject django_project  #to start project
tree
py manage.py runserver  ##to start  website
#to see all files in it
'''#http://127.0.0.1:8000/admin ##to see login page'''
'''
py manage.py startapp blog  #to to create new app with a name blog
/blog   ## to see blog page
add urls.py in blog folder
###########to create templates ###########
create templates folder in blog folder
blog--->templates-->blog-->templates.html
### touse templates we should add appsconfig to installed apps in settings.py of original ####
then add 'blog.apps.BlogConfig', in installed apps
### use render $#####
return render(request,'blog/home.html')  #in views
go to django model reference,charfield to see models
py manage.py makemigrations # to make migrations
'blog.apps.BlogConfig',  add to settings installed apps then do migrations command
py manage.py sqlmigrate blog 0001 to check ssql migration
py manage.py migrate # to migrate sql
py manage.py shell  #to play with our website to iterate over tutorials
from blog.models import Tutorial  ##to play iterate
Tutorial.objects.all()  ##to set query to see data
 new_tutorial =Tutorial(tutorial_title="to be",tutorial_content="...not to be",tutorial_published=timezone.now()) #i dont know
 new_tutorial.save()  #to save
 for t in Tutorial.objects.all():
   ...:     print(t.tutorial_title)    #to see what is sql
'''
'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/'''
