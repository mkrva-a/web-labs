"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваше город', min_length=2, max_length=100)
    job = forms.CharField(label='Ваше род занятий', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
                               choices=[('1','Мужской'),('2','Женский')],
                               widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Вы пользуетесь интернетом',
                                 choices=(('1','Каждый день'),
                                          ('2','Несколько раз в день'),
                                          ('3','Несколько раз в неделю'),
                                          ('4','Несколько раз в месяц')), initial=1)
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                               required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Коротко о себе',
                             widget=forms.Textarea(attrs={'rows':12, 'cols':20}))


class RecallForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    animal = forms.ChoiceField(label='У вас есть домашнее животное?',
                               choices=[('1','Да'),('2','Нет')],
                               widget=forms.RadioSelect, initial=1)
    message = forms.CharField(label='Поделитесь мнением о сайте нашего магазина',
                             widget=forms.Textarea(attrs={'rows':7, 'cols':20}))
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                               required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    products = forms.ChoiceField(label='Какие товары вы чаще всего покупаете',
                                 choices=(('1','Корм'),
                                          ('2','Игрушки'),
                                          ('3','Веттовары'),
                                          ('4','Уходовые товары')), initial=1)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':'Комментарий'}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': 'Заголовок','description':'Краткое содержание','content':'Полное содержание','image':'Картинка'}


    


