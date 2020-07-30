from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

# 별도로 View만들필요없이  django.contrib.auth의 LoginView를 사용한다.
# → 로그인 기능은 제공하지만 템플릿은 따로 제공하지 않아 직접생성.
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'),
]