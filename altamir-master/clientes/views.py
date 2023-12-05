from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse   
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from clientes.forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from clientes.models import User
from django.views.generic import CreateView, UpdateView


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'clientes/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('produtos:principal')

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, "USUÁRIO OU SENHA INVÁLIDOS!")
        return super().form_invalid(form)    


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'clientes/cadastro.html'
    success_url = '/'
    success_message = "Usuário Criado Com Sucesso!"


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ['email']
    template_name = 'clientes/atualizar.html'
    success_url = '/'
    success_message = 'Usuário criado!'

    def get_object(self, *args, **kwargs):
        user = super().get_object(*args, **kwargs)
        if not user.pk == self.request.user.pk:
            raise Http404
        return user


def deslogar(request):
    logout(request)
    return redirect(reverse('produtos:principal'))