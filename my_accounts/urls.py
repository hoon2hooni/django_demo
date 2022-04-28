from django.urls import path
from my_accounts import views

app_name='my_accounts'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('naver_test/',views.naver_test, name='naver_test')
]
