from django.urls import path
from . import views

app_name="landing"
urlpatterns = [
    path('', views.index, name="home"),
    path('<int:month>/', views.months),
    # path('<str:name>/', views.detail),
]
