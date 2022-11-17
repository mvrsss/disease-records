from django.urls import path, re_path
from specialize.views import SpecializeCreateView, SpecializeListView, SpecializeDetailView, SpecializeUpdateView, SpecializeDeleteView

urlpatterns = [
    path('create/', SpecializeCreateView.as_view(), name='specialize_create'),
    path('', SpecializeListView.as_view(), name='specialize_list'),
    re_path(r'^(?P<pk>\d+)/$', SpecializeDetailView.as_view(), name='specialize_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', SpecializeUpdateView.as_view(), name='specialize_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', SpecializeDeleteView.as_view(), name='specialize_delete')
]