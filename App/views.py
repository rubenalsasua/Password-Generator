import random
import secrets
import string

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from App.forms import PasswordForm
from App.models import Password


class PasswordListView(ListView):
    model = Password
    context_object_name = 'passwords'
    template_name = 'password_list.html'


class PasswordCreateView(CreateView):
    def get(selfs, request):
        formulario = PasswordForm()
        return render(request, 'password_create.html', {'formulario': formulario})

    def post(self, request):
        formulario = PasswordForm(request.POST)
        if formulario.is_valid():
            longitud_minima = formulario.cleaned_data['longitud_minima']
            longitud_maxima = formulario.cleaned_data['longitud_maxima']
            incluir_mayus_minus = formulario.cleaned_data['incluir_mayus_minus']
            incluir_digitos_especiales = formulario.cleaned_data['incluir_digitos_especiales']
            nueva_password = generar_password(longitud_minima, longitud_maxima, incluir_mayus_minus,
                                              incluir_digitos_especiales)
            Password.objects.create(password=nueva_password)
            return redirect('lista')
        return render(request, 'password_create.html', {'formulario': formulario})


def generar_password(min_length, max_length, inc_letras, inc_digitos_especiales):
    length = random.randint(min_length, max_length)

    if inc_letras:
        alphabet = string.ascii_letters
    else:
        alphabet = string.ascii_lowercase

    if inc_digitos_especiales:
        alphabet += string.digits + string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


class PasswordDeleteView(DeleteView):
    model = Password
    success_url = reverse_lazy('lista')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)
