from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'), 
    #path('<int:blog_id/>', views.detail, name='detail'), 
    path('home/', views.home, name="home"),
    path('blog', views.all_blogs, name="blog")
]
