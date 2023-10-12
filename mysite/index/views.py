from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView

from .forms import AddPostForm
from .forms import ContactForm
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


# <app name>/<model name>_list.html
class Home(ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Computer Games'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компьютерные игры'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Info.objects.filter(is_published=True)


# def main(request):
#     posts = Info.objects.all()
#     my_context = {
#         'title': 'Computer Games',
#         #'menu': menu,
#         'posts': posts,
#         'cat_selected':0
#     }
#     return render(request, 'index/index.html', context=my_context)


class CategoryPage(ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Компьютерные игры'
        context['cat_selected'] = context['posts'][0].category.pk
        return context

    def get_queryset(self):
        return Info.objects.filter(is_published=True, category__slug=self.kwargs['cat_slug'])


# def category(request, cat_slug):
#     posts = Info.objects.filter(category__slug = cat_slug)
#     if len(posts) == 0:
#         raise Http404()
#     my_context = {
#         'title': 'Computer Games',
#         #'menu': menu,
#         'posts': posts,
#         'cat_selected': posts[0].category.pk
#     }
#     return render(request, 'index/index.html', context=my_context)


# def category(request, catid=0):
#     if request.GET:
#         print(request.GET)
#     # if request.POST:
#     #     print(request.POST)
#     return HttpResponse(f'<h1>Category {catid}</h1>')
def post(request, post_slug):
    post = get_object_or_404(Info, slug = post_slug)
    my_context = {
        'title' : post.title,
        'post' : post,
        'cat_selected' : post.category.pk
    }
    return render(request, 'index/post.html', context=my_context)

def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                # Info.objects.create(**form.cleaned_data)
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = AddPostForm()
    my_context = {
        'title': "Добавление поста",
        'form': form
    }
    return render(request, 'index/addpost.html', context=my_context)


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка отправки')
    else:
        form = ContactForm()
    my_context = {
        'title': 'Связаться!',
        'address': ['ул. Пушкина, дом 121','г. Алматы, 123456'],
        'phone_nums': ['+7 701 755 67 67', '+7 727 3115468'],
        'opening_hours':['Понедельник-Пятница...10:00-20:00','суббота, воскресенье.....выходной'],
        'form': form
    }
    return render(request,'index/contact.html', context=my_context)

def login(request):
    return HttpResponse('Login Page')

def archive(request, year):
    if int(year) > 2022:
        # raise Http404()
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>archive {year}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')
