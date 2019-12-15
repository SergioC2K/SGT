from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, redirect
from django.urls import reverse

# Vistas = Listar y crear
from django.views.generic import ListView, CreateView, UpdateView

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User

# Forms

from usuario.forms import SignupForm, PerfilForm
from usuario.models import Perfil
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


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
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def perfil(request):
    return render(request, 'users/perfil.html')


# @user_passes_test(lambda u:u.is_staff, login_url=reverse('perfil'))
@login_required
def registrar(request):
    """Sign up view."""
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        email = request.POST['email']

        # este de dato tiene que ser 1 o 0
        is_staff = request.POST['cargo']
        username = request.POST['username']
        telefono_fijo = request.POST['telefono_fijo']
        celular = request.POST['celular']
        celular_telemercadeo = request.POST['celular_telemercadeo']
        cedula = request.POST['cedula']

        passwd = request.POST['password']
        passwd_confirmation = request.POST['cedula_confirmacion']

        if passwd != passwd_confirmation:
            return render(request, 'users/formulario.html', {'error': 'Password confirmation does not match'})

        else:
            user = User.objects.create_user(
                username=username,
                password=passwd,
                first_name=first_name,
                last_name=last_name,
                email=email,
                is_staff=is_staff,
            )

            profile = Perfil(
                usuario=user,
                cedula=cedula,
                telefono_fijo=telefono_fijo,
                celular=celular,
                celular_telemercadeo=celular_telemercadeo,
            )

            user.save()
            profile.save()

            return redirect('usuario:listar_usuario')

    return render(request, 'users/formulario.html')


@login_required
def actualizar_usuario(request):
    perfil = request.user.perfil
    esto = request.user

    if request.method == 'POST':

        form = PerfilForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            perfil.usuario.first_name = data['nombre']
            perfil.usuario.last_name = data['apellido']
            perfil.cedula = data['cedula']
            perfil.celular_telemercadeo = data['celular_telemercadeo']
            perfil.celular = data['celular']
            perfil.telefono_fijo = data['telefono_fijo']

            perfil.save()
            esto.save()
            return redirect('usuario:login')
        else:
            return render(request=request,
                          template_name='users/perfil.html',
                          context={
                              'perfil': perfil,
                              'usuario': request.user,
                              'form': form,
                              'errors': 'La contraseña no coincide'
                          }, )
    else:
        form = PerfilForm()
    return render(
        request=request,
        template_name='users/perfil.html',
        context={
            'perfil': perfil,
            'usuario': request.user,
            'form': form
        },
    )


@login_required
def cambio_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('usuario:logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/nuevaContraseña', {
        'form': form
    })


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('usuario:login')


"""class listar_usuario(ListView):
    model = Perfil
    template_name = 'users/listar.html'"""

"""@login_required
def listar_usuario(request):
    array = Perfil.objects.all()
    if array:
        contexto = {'lista': array}
        return render(request, 'users/listar.html', contexto)
    return render(request, 'users/listar.html', {'error': 'No hay datos'})"""


class listar_usuario(ListView):
    model = Perfil
    template_name = 'users/listar.html'


# @user_passes_test(lambda u:u.is_staff, login_url=('perfil'))
@login_required
def deshabilitar(request, id):
    django = User.objects.get(pk=id)

    if django.is_active:
        django.is_active = False
        django.save()
    else:
        django.is_active = True
        django.save()

    return render(request, template_name='users/listar.html')

