"""
Definition of urls for lab4.
"""
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    url(r'^anketa$',views.anketa,name='anketa'),
    url(r'^recall$',views.recall,name='recall'),
    url(r'^newpost$',views.newpost,name='newpost'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^blog',views.blog, name='blog'),
    path('video/', views.video, name='video'),
    path('admin/', admin.site.urls),
    url(r'^(?P<parametr>\d+)/$', views.blogpost, name = 'blogpost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()