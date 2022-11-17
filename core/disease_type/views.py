from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from disease_type.models import DiseaseType
from django.urls import reverse_lazy
from disease_type.forms import DiseaseTypeForm

class DiseaseTypeListView(ListView):
    model = DiseaseType
    context_object_name = 'disease_type'

class DiseaseTypeDetailView(DetailView):
    model = DiseaseType

class DiseaseTypeCreateView(CreateView):
    model = DiseaseType
    form_class = DiseaseTypeForm
    success_url = reverse_lazy('disease_type_list')

class DiseaseTypeUpdateView(UpdateView):
    model = DiseaseType
    form_class = DiseaseTypeForm
    success_url = reverse_lazy('disease_type_list')

class DiseaseTypeDeleteView(DeleteView):
    model = DiseaseType
    success_url = reverse_lazy('disease_type_list')