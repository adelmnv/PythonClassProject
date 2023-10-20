from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', main, name = 'home'),
    path('', HomeView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('login/', login, name = 'login'),
    path('post/<slug:post_slug>', PostView.as_view(), name = 'post'),
    path('category/<slug:cat_slug>', CategoryView.as_view(), name = 'category'),
    path('addpost/', AddPostView.as_view(), name = 'addpost')
    # path('category/', category),
    # path('category/<slug:catid>', category),
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive)
]