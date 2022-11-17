from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Doctor
from django.urls import reverse_lazy
from doctor.forms import DoctorForm

class DoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctor'

class DoctorDetailView(DetailView):
    model = Doctor

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('doctor_list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctor_list')