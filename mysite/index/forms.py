from django import forms
from django.core.exceptions import ValidationError

from .models import *

# class AddPostForm(forms.Form):
    # title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form__input'}))
    # slug = forms.SlugField(max_length=255, label='URL')
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows':10}),label='Контент', required=False)
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категория', empty_label='Выберите категорию')


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Info
        fields = ['title', 'slug', 'content', 'is_published', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input'}),
            'content': forms.Textarea(attrs={'class': 'form__input'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Длина превышает 20 символов')
        return title



class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Введите ваше имя','class': 'contact__form__input' }))
    email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Введите ваш email','class': 'contact__form__input'}))
    message = forms.CharField( widget=forms.Textarea(attrs={'placeholder':'Введите ваше сообщение', 'class': 'contact__form__input', 'cols': 60,'rows':10}))