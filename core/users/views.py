from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import User
from django.urls import reverse_lazy
from users.forms import UserForm

class UserListView(ListView):
    model = User
    context_object_name = 'user'

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')