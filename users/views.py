import os

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.views import View

from .forms import UserRegistrationForm, EmailLoginForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)

            send_mail(
                "Добро пожаловать!",
                "Спасибо за регистрацию в нашем сервисе.",
                os.getenv("EMAIL"),  # Отправитель
                [user.email],  # Получатель
                fail_silently=False,
            )
            messages.success(request, "Регистрация прошла успешно! Добро пожаловать.")
            return redirect("catalog:home")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = EmailLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("catalog:home")
    else:
        form = EmailLoginForm()
    return render(request, "users/login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("catalog:home")
