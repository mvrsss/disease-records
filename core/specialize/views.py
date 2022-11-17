from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Specialize
from django.urls import reverse_lazy
from specialize.forms import SpecializeForm

class SpecializeListView(ListView):
    model = Specialize
    context_object_name = 'specialize'

class SpecializeDetailView(DetailView):
    model = Specialize

class SpecializeCreateView(CreateView):
    model = Specialize
    form_class = SpecializeForm
    success_url = reverse_lazy('specialize_list')

class SpecializeUpdateView(UpdateView):
    model = Specialize
    form_class = SpecializeForm
    success_url = reverse_lazy('specialize_list')

class SpecializeDeleteView(DeleteView):
    model = Specialize
    success_url = reverse_lazy('specialize_list')