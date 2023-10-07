from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


# Create your views here.

# menu = [
#     {'title' : 'Главная', 'url_name' : 'home'},
#     {'title' : 'О компании','url_name' : 'about'},
#     {'title' : 'Контакты', 'url_name' : 'contact'},
#     {'title' : 'Login', 'url_name' : 'login'},
# ]

# def main(request):
#     #return HttpResponse("Hello world!")
#     return render(request, 'index/index.html', {'title':'Добро пожаловать', 'menu':menu})

def main(request):
    posts = Info.objects.all()
    my_context = {
        'title': 'Computer Games',
        #'menu': menu,
        'posts': posts,
        'cat_selected':0
    }
    return render(request, 'index/index.html', context=my_context)



def about(request):
    # Отображение шаблоном
    # шаблоны находятся в папке templates
    # в templates обязательно должна быть папка с названием страницы или приложения
    my_context = {
        'title': 'Computer Games',
        #'menu': menu,
    }
    return render(request,'index/about.html', context=my_context)

def contact(request):
    return HttpResponse('Contact Page')

def login(request):
    return HttpResponse('Login Page')


def category(request, cat_id):
    posts = Info.objects.filter(category_id = cat_id)
    if len(posts) == 0:
        raise Http404()
    my_context = {
        'title': 'Computer Games',
        #'menu': menu,
        'posts': posts,
        'cat_selected': cat_id
    }
    return render(request, 'index/index.html', context=my_context)


# def category(request, catid=0):
#     if request.GET:
#         print(request.GET)
#     # if request.POST:
#     #     print(request.POST)
#     return HttpResponse(f'<h1>Category {catid}</h1>')
def post(request, post_id):
    post = get_object_or_404(Info, pk = post_id)
    my_context = {
        'title' : post.title,
        'post' : post,
        'cat_selected' : post.category.pk
    }
    return render(request, 'index/post.html', context=my_context)



def archive(request, year):
    if int(year) > 2022:
        # raise Http404()
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>archive {year}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')
