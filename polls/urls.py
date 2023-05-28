from django.urls import path, include
from . import views
from django.urls import re_path

app_name = 'polls'
urlpatterns = [
    #path('details/', views.detail, name='detail'),
    #path('results/', views.results, name='results'),
    #path('vote/', views.vote, name='vote'),
    path('', views.index, name='index'),
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #re_path(r'^blog/(?P<year>[0-9]{4})/$',views.blog_detail)
]


