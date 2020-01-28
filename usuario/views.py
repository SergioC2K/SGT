from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core import serializers

from django.views.generic import ListView, FormView

from usuario.forms import SignupForm, PerfilForm
from usuario.models import Perfil
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


class LoginViewUsuario(LoginView):

    template_name = 'users/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('usuario:perfil')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('usuario:perfil'))
        return super(LoginViewUsuario, self).get(request, *args, **kwargs)


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            return redirect('usuario:perfil')

        else:
            return render(request, 'users/login.html', {'error': 'Usuario y/o contraseña invalido'})

    return render(request, 'users/login.html')


def perfil(request):
    return render(request, 'users/perfil.html')


class PerfilCreateView(FormView):
    template_name = 'users/perfil.html'
    form_class = PerfilForm
    success_url = reverse_lazy('usuario:listar_usuario')


class UserCreateView(FormView):
    template_name = 'users/usuario_nuevo.html'
    form_class = SignupForm
    success_url = reverse_lazy('usuario:listar_usuario')

    def form_valid(self, form):
        """Guardar datos."""
        form.save()
        return super().form_valid(form)


@login_required
def cambio_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contrasena ha sido cambiada!')
            return redirect('usuario:logout')
        else:
            messages.error(request, 'Por favor corrija el error a continuación.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/nuevaContrasena.html', {
        'form': form
    })


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('usuario:login')


class listar_usuario(ListView):
    model = Perfil
    template_name = 'users/listar.html'
    queryset = Perfil.objects.filter(usuario__is_superuser=False)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Perfil.objects.all()
        else:
            return Perfil.objects.filter(usuario__is_superuser=False)


# @user_passes_test(lambda u:u.is_staff, login_url=('perfil'))
@login_required
def deshabilitar(request):
    if request.method == 'POST':
        usuario = request.user
        if usuario.is_active:
            usuario.is_active = False
            usuario.save()
        else:
            usuario.is_active = True
            usuario.save()

    url = reverse('usuario:listar_usuario')

    return redirect(url)


def conectado(request):
    persona = request.user.perfil
    persona.conexion.estado = True
    persona.conexion.save()
    url = reverse('usuario:perfil')
    return redirect(url)


def desconectado(request):
    persona = request.user.perfil
    persona.conexion.estado = False
    persona.conexion.save()
    url = reverse('usuario:perfil')
    return redirect(url)


class ListEstado(ListView):
    template_name = 'prueba.html'
    model = Perfil

    def get(self, request, *args, **kwargs):
        name = request.GET['name']
        perfiles = Perfil.objects.get(usuario__first_name=name)
        data = serializers.serialize('json', perfiles, fields=('first_name', 'is_superuser'))
        return HttpResponse(data, content_type='application/json')
