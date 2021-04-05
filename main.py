# This is a sample Python script.
#https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog to see coreyschafer guthub
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
######## to add context without template ###########################
add dictionaires in views 
then add context in views,then in home html for loop contents

############tut 3 ADMIN PAGES ################
py manage.py createsuperuser  #THROWS ERROR no such table: auth_user BECAUSE WE HAVENT CREATED DB YET
py manage.py makemigrations  #we havent added db yet detect changes
py manage.py migrate  ##now we can use admin page
py manage.py createsuperuser  #add user passwd email    

######### DB AND MIGRATIONS ############
ORM OBJECT REATIONAL MATTER
SQLLITE FOR DEVELOPMENT ,POSTGRESQL FOR PRODUCITON
WE HAVE MADE MODEL AND NOW WE NEED TO MIGRATE IT TO DB
py manage.py makemigrations  #SO WE USE THIS COMMAND
py manage.py sqlmigrate blog 0001 #to ssee how model code exctes in sql code
py manage.py migrate   #to migrate to DB

from blog.models import Post
 from django.contrib.auth.models import User
 User.objects.all()
 User.objects.first()
Out[4]: <User: naresh>

In [5]: User.objects.filter(username='naresh')
Out[5]: <QuerySet [<User: naresh>]>

In [6]: User.objects.filter(username='naresh').first()
Out[6]: <User: naresh>

In [7]: user=User.objects.filter(username='naresh').first()  
 user
Out[8]: <User: naresh>

In [9]: user.id
Out[9]: 1

In [10]: user.pk
Out[10]: 1

In [11]: user= User.objects.get(id=1)

In [12]: user
Out[12]: <User: naresh>

In [13]: Post.objects.all()
Out[13]: <QuerySet []>

In [14]: post_1 = Post(title='Blog_1',content='First post content' 
    ...: ,author=user)

In [15]: Post.objects.all()
Out[15]: <QuerySet []>


In [19]: post_1.save()

In [20]: Post.objects.all()
Out[20]: <QuerySet [<Post: Post object (1)>]>
v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information      
IPython 7.21.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from blog.models import Post

In [2]: from django.contrib.auth.models import User

In [3]: Post.objects.all()
Out[3]: <QuerySet [<Post: Blog_1>]>

In [4]: user = User.objects.filter(username='naresh').first()      

In [5]: user
Out[5]: <User: naresh>


In [7]: post_2 = Post(title='Blog 2',content='Second Post Content' 
   ...: ,author_id=user.id)

In [8]: post_2
Out[8]: <Post: Blog 2>

In [9]: post_2.save()

In [10]: Post.objects.all()
Out[10]: <QuerySet [<Post: Blog_1>, <Post: Blog 2>]>

In [11]: post = Post.objects.first()

In [12]: post.content
Out[12]: 'First post content'

In [13]: post.date_posted
Out[13]: datetime.datetime(2021, 4, 2, 5, 26, 21, 794766, tzinfo=<UTC>)

In [14]: post.author
Out[14]: <User: naresh>

In [15]: post.author.email
Out[15]: 'djangonaresh123@gmail.com'

In [16]: user
Out[16]: <User: naresh>

In [17]: user.post_set
Out[17]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x163e0f37c40>    

In [18]: user.post_set.all
Out[18]: <bound method BaseManager.all of <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x00000163E0EDC190>>

In [19]: user.post_set.all()
Out[19]: <QuerySet [<Post: Blog_1>, <Post: Blog 2>]>

In [20]: user.post_set.create(title='Blog 3',content='Third post c 
    ...: ontent!')
Out[20]: <Post: Blog 3>

In [21]: Post.objects.all()
Out[21]: <QuerySet [<Post: Blog_1>, <Post: Blog 2>, <Post: Blog 3>]>

####      user registration ######
post request # to get user data
get request #simply display a page
crispy forms allow us to style our form
pip install django-crispy-forms

################ userprofile and picture ##############
from django.contrib.auth.models import User

In [1]: from django.contrib.auth.models import User

In [2]: user =User.objects.filter(username='naresh').first()    

In [3]: user
Out[3]: <User: naresh>
       

In [5]: user.profile
Out[5]: <Profile: naresh Profile>

In [6]: user.profile.image
Out[6]: <ImageFieldFile: profile_pics/WIN_20200807_11_31_58_Pro.jpg>

In [7]: user.profile.image.width
Out[7]: 1280

In [8]: user.profile.image.url
Out[8]: '/profile_pics/WIN_20200807_11_31_58_Pro.jpg'

In [9]: user =User.objects.filter(username='newuser3').first()  

In [10]: user
Out[10]: <User: newuser3>

In [11]: user.profile.image

### to see django static files doc
https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development

####### pagination adding posts with json ##########################

In [1]: import json

In [2]: from blog.models import Post

In [3]: with open('posts.json') as f:
   ...: 

In [4]: for post in posts_json:
   ...:     post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
   ...:     post.save()
   ...: 

In [5]: exit
##############using paginator  ##############
 from django.core.paginator import Paginator

In [2]: posts = ['1','2','3','4','5']

In [3]: p =Paginator(posts, 2)

In [4]: p.num_pages
Out[4]: 3

In [5]: for page in p.page_range:
   ...:     print(page)
   ...: 
1
2
3


In [6]: p1= p.page(1)

In [7]: 

In [7]: p1
Out[7]: <Page 1 of 3>

In [8]: p1.number
Out[8]: 1

In [9]: p1.object_list
Out[9]: ['1', '2']

In [10]: p1.has_previous()
Out[10]: False

In [11]: p1.has_next()
Out[11]: True

In [13]: p1.next_page_number()
Out[13]: 2
http://127.0.0.1:8000/?page=14  ## to check posts on server


############ EMAIL AND PASSWORD RESET ###################
http://127.0.0.1:8000/password-reset/ ##to reset password

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
