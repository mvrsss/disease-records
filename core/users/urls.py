from django.urls import path, re_path
from users.views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('', UserListView.as_view(), name='user_list'),
    re_path(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='user_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='user_delete')
]