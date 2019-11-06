from django.urls import path,include

from blogapp.views import *

urlpatterns = [

   path("", home),
   
   path("blog/", blogpage, name="blog"),

   path("login/",  signin),
   
   path("signup/", signup),

   path("all-posts/", get_all_posts),

   path("make-post/", make_post),

   path("delete-post/<int:post_id>/", delete_post),

   path("signout/", signout),

   path('oauth/', include('social_django.urls', namespace='social')),

]