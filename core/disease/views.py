from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from disease.models import Disease
from django.urls import reverse_lazy
from disease.forms import DiseaseForm

class DiseaseListView(ListView):
    model = Disease
    context_object_name = 'disease'

class DiseaseDetailView(DetailView):
    model = Disease

class DiseaseCreateView(CreateView):
    model = Disease
    form_class = DiseaseForm
    success_url = reverse_lazy('disease_list')

class DiseaseUpdateView(UpdateView):
    model = Disease
    form_class = DiseaseForm
    success_url = reverse_lazy('disease_list')

class DiseaseDeleteView(DeleteView):
    model = Disease
    success_url = reverse_lazy('disease_list')