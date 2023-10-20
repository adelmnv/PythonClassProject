from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView

from .forms import AddPostForm, RegisterUserForm
from .forms import ContactForm
from .models import *
from .utils import *

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
class HomeView(DataMixin, ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Computer Games'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Компьютерные игры'
        # context['cat_selected'] = 0
        c_def = self.get_user_context(title = 'Компьютерные игры')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Info.objects.filter(is_published=True).select_related('category')


# def main(request):
#     posts = Info.objects.all()
#     my_context = {
#         'title': 'Computer Games',
#         #'menu': menu,
#         'posts': posts,
#         'cat_selected':0
#     }
#     return render(request, 'index/index.html', context=my_context)


class CategoryView(DataMixin, ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    allow_empty = False
    def get_queryset(self):
        return Info.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True).select_related('category')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['posts'][0].category),
                                      cat_selected = context['posts'][0].category.pk)
        return dict(list(context.items()) + list(c_def.items()))




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


class PostView(DataMixin, DetailView):
    model = Info
    template_name = 'index/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['title'] = context['post']
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

# def post(request, post_slug):
#     post = get_object_or_404(Info, slug = post_slug)
#     my_context = {
#         'title' : post.title,
#         'post' : post,
#         'cat_selected' : post.category.pk
#     }
#     return render(request, 'index/post.html', context=my_context)


class AddPostView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'index/addpost.html'
    success_url = reverse_lazy('home')
    #login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = "Добавление поста"
        # return context
        c_def = self.get_user_context(title='Добавление поста')
        return dict(list(context.items()) + list(c_def.items()))


# def addpost(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 # Info.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления')
#     else:
#         form = AddPostForm()
#     my_context = {
#         'title': "Добавление поста",
#         'form': form
#     }
#     return render(request, 'index/addpost.html', context=my_context)


class AboutView(DataMixin, TemplateView):
    template_name = 'index/about.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'О компании'
        about_desc = 'Компания, специализирующаяся на продаже компьютерных игр, предоставляет широкий ассортимент игровых продуктов для разнообразных платформ. Наш сайт предлагает удобное и надежное место для покупки и загрузки игр, позволяя клиентам мгновенно получить доступ к желанным развлечениям. Мы предоставляем постоянные обновления, специальные предложения и скидки, чтобы сделать покупку игр еще более привлекательной. Наш сайт также обеспечивает безопасную и надежную среду для оплаты, а наша команда готова помочь вам с любыми вопросами и запросами. Приходите и наслаждайтесь миром игр с нами!'
        c_def = self.get_user_context(title='О компании', desc = about_desc)
        return dict(list(context.items()) + list(c_def.items()))


# def about(request):
#     # Отображение шаблоном
#     # шаблоны находятся в папке templates
#     # в templates обязательно должна быть папка с названием страницы или приложения
#     my_context = {
#         'title': 'Computer Games',
#         #'menu': menu,
#     }
#     return render(request,'index/about.html', context=my_context)

class ContactView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'index/contact.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = "Связаться!"
        # context['address'] = ['ул. Пушкина, дом 121','г. Алматы, 123456']
        # context['phone_nums'] = ['+7 701 755 67 67', '+7 727 3115468']
        # context['opening_hours'] = ['Понедельник-Пятница...10:00-20:00','суббота, воскресенье.....выходной']
        c_def = self.get_user_context(title="Связаться!", address=['ул. Пушкина, дом 121','г. Алматы, 123456'], phone_nums = ['+7 701 755 67 67', '+7 727 3115468'], opening_hours = ['Понедельник-Пятница...10:00-20:00','суббота, воскресенье.....выходной'])
        return dict(list(context.items()) + list(c_def.items()))

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             try:
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка отправки')
#     else:
#         form = ContactForm()
#     my_context = {
#         'title': 'Связаться!',
#         'address': ['ул. Пушкина, дом 121','г. Алматы, 123456'],
#         'phone_nums': ['+7 701 755 67 67', '+7 727 3115468'],
#         'opening_hours':['Понедельник-Пятница...10:00-20:00','суббота, воскресенье.....выходной'],
#         'form': form
#     }
#     return render(request,'index/contact.html', context=my_context)

class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'index/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

def login(request):
    return HttpResponse('Login Page')

# @login_required - ограничить доступ для функций
def archive(request, year):
    if int(year) > 2022:
        # raise Http404()
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>archive {year}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')
