from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Discover
from django.urls import reverse_lazy
from discover.forms import DiscoverForm

class DiscoverListView(ListView):
    model = Discover
    context_object_name = 'discover'

class DiscoverDetailView(DetailView):
    model = Discover

class DiscoverCreateView(CreateView):
    model = Discover
    form_class = DiscoverForm
    success_url = reverse_lazy('discover_list')

class DiscoverUpdateView(UpdateView):
    model = Discover
    form_class = DiscoverForm
    success_url = reverse_lazy('discover_list')

class DiscoverDeleteView(DeleteView):
    model = Discover
    success_url = reverse_lazy('discover_list')