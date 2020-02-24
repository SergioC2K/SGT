from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core import serializers
from django.utils.decorators import method_decorator

from django.views.generic import ListView, FormView

# Vistas = Listar y crear
from django.views.generic import ListView, CreateView, UpdateView, FormView

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User

from django.contrib import messages

# Forms
from django.views.generic.edit import FormMixin

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
            messages.success(request, f"Bienvenido: {Perfil.usuario}")
            return HttpResponseRedirect(reverse_lazy('usuario:perfil'))
        return super(LoginViewUsuario, self).get(request, *args, **kwargs)


def perfil(request):
    return render(request, 'users/perfil.html')


def UserCreateView(request):
    if request.is_ajax():
        formula = SignupForm(request.POST)
    if formula.is_valid():
        guardar = formula.save()
    data = {'estado': 'guardado'}
    return JsonResponse(data)


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


superuser_required = user_passes_test(lambda u: u.is_staff, login_url=('usuario:perfil'))


@method_decorator(superuser_required, name='dispatch')
class ListarUsuario(ListView, FormView):
    model = Perfil
    form_class = SignupForm
    template_name = 'users/listar.html'
    queryset = Perfil.objects.filter(usuario__is_superuser=False)
    success_url = reverse_lazy('usuario:listar_usuario')


def get_queryset(self):
    if self.request.user.is_superuser:
        return Perfil.objects.all()
    else:
        return Perfil.objects.filter(usuario__is_superuser=False)


def form_valid(self, form):
    """Guardar datos."""
    form.save()

    return super().form_valid(form)



# @user_passes_test(lambda u:u.is_staff, login_url=('perfil'))
@login_required
def deshabilitar(request):
    if request.method == 'POST':
        usuario_pk = request.POST['user']
        user = User.objects.get(pk=usuario_pk)
        if user.is_active:
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()

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


class UpdateProfileView(UpdateView):
    """Update profile view."""
    template_name = 'users/perfil.html'
    model = Perfil
    form_class = PerfilForm
    success_url = reverse_lazy('usuario:listar_usuario')

    def get_object(self, **kwargs):
        """Return user's profile."""
        return self.request.user.perfil

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.usuario.username
        return reverse('usuario:listar_usuario')
