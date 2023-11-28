from django.shortcuts import render




def index(reguest): #httpReguest
    return render(reguest,'index.html')

def authorization(reguest):
    return render(reguest, 'authorization.html')

#def login(reguest):
 #   return render(reguest, 'login.html')

def logout(reguest):
    return render(reguest, 'logged_out.html')

def profile(reguest):
    return render(reguest, 'index.html')

#def register(reguest):
#    return render(reguest, 'register.html')

def help(reguest):
    return render(reguest, 'help.html')

def monitoring(reguest):
    return render(reguest, 'monitoring.html')

def test(reguest):
    return render(reguest, 'test.html')


from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .form import UserLoginForm


class UserLoginView(SuccessMessageMixin, LoginView):

    form_class = UserLoginForm
    template_name = 'system/user_login.html'
    next_page = 'home'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context

#------------------------------------
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .form import UserRegisterForm


class UserRegisterView(SuccessMessageMixin, CreateView):

    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'system/user_register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context
