from django.contrib import admin
from django.urls import path,re_path,include
from django3app import views

postslist = [
    path("popular-posts/",views.popposts),
    path("last-posts/",views.lastposts),
    path("all-posts/",views.allposts),
    path("",views.posts),

]
arg = [
    path("likecomm/", views.likecomm),
    path("", views.posts),

]
urlpatterns = [
    path('',views.index),
    path("posts/<int:id>/",include(arg)),
    path("posts/",include(postslist)),
    path("about/", views.about),
    path("contacts/", views.contacts),
    path("err/",views.err),
    path("access/",views.access),
    path("json/",views.json)
]


