from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name = 'home'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('login/', login, name = 'login'),
    path('post/<int:post_id>', post, name = 'post'),
    path('post/<int:cat_id>', category, name = 'category'),
    # path('category/', category),
    # path('category/<slug:catid>', category),
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive)
]