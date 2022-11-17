from django.urls import path, re_path
from discover.views import DiscoverCreateView, DiscoverListView, DiscoverDetailView, DiscoverUpdateView, DiscoverDeleteView

urlpatterns = [
    path('create/', DiscoverCreateView.as_view(), name='discover_create'),
    path('', DiscoverListView.as_view(), name='discover_list'),
    re_path(r'^(?P<pk>\d+)/$', DiscoverDetailView.as_view(), name='discover_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', DiscoverUpdateView.as_view(), name='discover_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', DiscoverDeleteView.as_view(), name='discover_delete')
]