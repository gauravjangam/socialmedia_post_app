from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('twitter_post',views.twitter_post,name="twitter_post"),
    path('facebook_post',views.facebook_post,name="facebook_post"),
]
