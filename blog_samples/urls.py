from django.urls import path
from . import views


from blog_samples import views
app_name="blog_samples"
urlpatterns = [
    path('', views.index, name="home"),
    path('post/', views.post, name="post"),
    path('about/', views.contact, name="contact"),
]
