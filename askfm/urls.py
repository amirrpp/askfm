"""askfm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from answer.views import UserListView, UserQuestionListView, CreateUserQuestion, CreateAnswer

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', UserListView.as_view(), name='home'),
    url(r'^(?P<user_pk>\d+)/$', UserQuestionListView.as_view(), name='user_questions'),
    url(r'^(?P<user_pk>\d+)/(?P<pk>\d+)/$', CreateAnswer.as_view(), name='question_answer'),
    url(r'^(?P<user_pk>\d+)/add_question/$', CreateUserQuestion.as_view(), name='add_question'),
]
