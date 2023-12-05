from django.urls import path
from . import views
from clientes.views import UserLoginView, UserCreateView, UserUpdateView

app_name = 'clientes'

urlpatterns = [
    path('', UserLoginView.as_view(), name="login"),
    path('<int:pk>/atualizar', UserUpdateView.as_view(), name='atualizar_cliente'),
    path('cadastro/', UserCreateView.as_view(), name="cadastro"),
    path('sair/', views.deslogar, name="deslogar")
]