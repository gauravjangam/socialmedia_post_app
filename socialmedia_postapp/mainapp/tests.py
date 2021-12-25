from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import home,twitter_post,facebook_post


class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url = reverse('home')   
        self.assertEquals(resolve(url).func, home)

    def test_twitter_post_url(self):
        twitter_url = reverse('twitter_post')   
        self.assertEquals(resolve(twitter_url).func, twitter_post)

    def test_facebook_post_url(self):
        facebook_url = reverse('facebook_post')   
        self.assertEquals(resolve(facebook_url).func, facebook_post)

