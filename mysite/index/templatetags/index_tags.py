from django import template
from index.models import *

register = template.Library()


@register.simple_tag(name = 'getcats')
def get_categories(filter = None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk = filter)


@register.inclusion_tag('index/list_categories.html')
def show_categories(sort = None, cat_selected = 0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats' : cats, 'cat_selected' : cat_selected}


@register.inclusion_tag('index/list_menu.html')
def show_menu():
    menu = [
        {'title': 'Главная', 'url_name': 'home'},
        {'title': 'О компании', 'url_name': 'about'},
        {'title': 'Добавление поста', 'url_name': 'addpost'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}
    ]
    return {'menu':menu}


@register.inclusion_tag('index/footer.html')
def show_footer():
    menu = [
        {'title': 'Главная', 'url_name': 'home'},
        {'title': 'О компании', 'url_name': 'about'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        {'title': 'Добавление поста', 'url_name' : 'addpost'}
    ]
    about = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id quam ut metus bibendum suscipit. Aliquam erat volutpat. Fusce eleifend justo id lacus scelerisque, ac bibendum justo consequat. Nunc euismod arcu in dolor consectetur, ac rhoncus augue malesuada. Nulla facilisi. Maecenas in ligula sit amet arcu consectetur aliquet. Quisque sit amet magna vel libero ultrices tincidunt.'
    return {'menu': menu, 'about' : about}

