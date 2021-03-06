from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #개별적으로 데이터 얻기
            raw_password = form.cleaned_data.get('password1') #개별적으로 데이터 얻기
            user = authenticate(username=username, password=raw_password) #가입후 자동으로 로그인되도록.
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})