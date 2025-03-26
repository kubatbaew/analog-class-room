from django.shortcuts import render, redirect

from django.contrib.auth import logout, authenticate, login


def logout_logics(request):
    logout(request)
    return redirect('login')


def login_logics(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        error = "Неправильный логин или пароль!"
        return render(request, 'pages/auth/login.html', locals())

    return render(request, 'pages/auth/login.html', locals())
