from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Proveedor, CategoriaIndustria
from .forms import ProveedoresForm, LoginForm


# Create your views here.


def log_in(request):
    # Diccionario que almacena los datos que enviamos a la vista
    form = LoginForm(
        request.POST or None
    )
    context = {'message': None, 'form': form}
    if request.POST and form.is_valid():
        # Verificar credenciales
        # Devuelve un objeto User si las credenciales son válidas.
        # Si las credenciales no son válidas, devuelve None
        user = authenticate(**form.cleaned_data)
        if user is not None:
            # Verificar si el usuario esta activo
            if user.is_active:
                # Adjuntar usuario autenticado a la sesión actual
                login(request, user)
                # Redireccionar a una vista utilizando el nombre de la url
                return redirect('proveedores:home')
            else:
                context['message'] = 'El usuario ha sido desactivado'
        else:
            context['message'] = 'Usuario o contraseña incorrecta'
    return render(request, 'proveedores/login.html', context)


# decorador para restringir el acceso a solo usuarios autenticados
@login_required
def log_out(request):
    logout(request)
    return redirect('proveedores:log-in')


@login_required
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/index.html', {'proveedores': proveedores})


@login_required
def proveedor_detail(request, pk):
    try:
        # recuperamos el objeto mediante la
        # API de abstracción de base de datos
        # que ofrece Django
        m = Proveedor.objects.get(pk=pk)
    except Proveedor.DoesNotExist:
        raise Http404("No existe el proveedor")

    # version con shortcuts de django, equivalente al codigo anterior
    # m = get_object_or_404(Proveedor, pk=pk) OJO AQUI ANTES DE LA M
    return render(request, 'proveedores/detail.html', {'proveedores': m})


@login_required
def proveedor_create(request, **kwargs):
    # Intanciamos la clase form
    # si el diccionario request.POST no esta vacio
    # la instancia se creara con dichos datos, sino estara vacia
    form = ProveedoresForm(
        request.POST or None,
        request.FILES or None
    )
    # Comprobamos que la peticion es del motodo POST
    # y que el formulario es valido
    if request.POST and form.is_valid():
        # Guardamos el objeto
        form.save()
        # redirigir a una nueva URL
        return redirect('proveedores:home')
    return render(request, 'proveedores/form.html', {'form': form})


@login_required
def proveedor_update(request, **kwargs):
    # recuperamos el objeto a actualizar
    proveedor = Proveedor.objects.get(pk=kwargs.get('pk'))
    # inicializamos el formulario con el objeto recuperado
    form = ProveedoresForm(
        request.POST or None,
        instance=proveedor
    )
    if request.POST and form.is_valid():
        form.save()
        return redirect('proveedores:home')
    return render(request, 'proveedores/form.html', {'form': form})


@login_required
def proveedor_delete(request, **kwargs):
    proveedor = Proveedor.objects.get(pk=kwargs.get('pk'))
    proveedor.delete()
    return redirect('proveedores:home')


@login_required
def category_list(request):
    categories = CategoriaIndustria.objects.all()
    return render(request, 'proveedores/category/category_list.html', {'categories': categories})