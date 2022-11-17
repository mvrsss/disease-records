from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from countries.models import Country
from django.urls import reverse_lazy
from countries.forms import CountryForm

class CountryListView(ListView):
    model = Country
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    model = Country

class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('country_list')

class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('country_list')

class CountryDeleteView(DeleteView):
    model = Country
    success_url = reverse_lazy('country_list')