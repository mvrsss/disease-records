from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import PublicServant
from django.urls import reverse_lazy
from publicservant.forms import PublicServantForm

class PublicServantListView(ListView):
    model = PublicServant
    context_object_name = 'publicservant'

class PublicServantDetailView(DetailView):
    model = PublicServant

class PublicServantCreateView(CreateView):
    model = PublicServant
    form_class = PublicServantForm
    success_url = reverse_lazy('publicservant_list')

class PublicServantUpdateView(UpdateView):
    model = PublicServant
    form_class = PublicServantForm
    success_url = reverse_lazy('publicservant_list')

class PublicServantDeleteView(DeleteView):
    model = PublicServant
    success_url = reverse_lazy('publicservant_list')