import tweepy
import facebook

from django.conf import settings
from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    return render(request,"index.html")

def twitter_post(request):
    if request.method == 'POST':

        content = request.POST.get('content', '')
        if content:

            auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
            auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

            api = tweepy.API(auth)
            api.update_status(content)

            print('Content:', content)
            return redirect('home')

    return render(request,'twitter_post.html')

def facebook_post(request):
    if request.method == 'POST':

        fb_content = request.POST.get('fb_content')
        if fb_content:

            fb_api = facebook.GraphAPI(settings.FB_ACCESS_TOKEN)
            fb_api.put_object("me","feed",message=fb_content)

            print('Facebook_Content:', fb_content)
            return redirect('home')

    return render(request,'facebook_post.html')