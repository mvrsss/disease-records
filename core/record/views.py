from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Record
from django.urls import reverse_lazy
from record.forms import RecordForm

class RecordListView(ListView):
    model = Record
    context_object_name = 'record'

class RecordDetailView(DetailView):
    model = Record

class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('record_list')

class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('record_list')

class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('record_list')