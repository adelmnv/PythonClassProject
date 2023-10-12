from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('', main, name = 'home'),
    path('', Home.as_view(), name = 'home'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('login/', login, name = 'login'),
    path('post/<slug:post_slug>', post, name = 'post'),
    path('category/<slug:cat_slug>', CategoryPage.as_view(), name = 'category'),
    path('addpost/', addpost, name = 'addpost')
    # path('category/', category),
    # path('category/<slug:catid>', category),
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive)
]