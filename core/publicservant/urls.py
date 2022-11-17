from django.urls import path, re_path
from publicservant.views import PublicServantCreateView, PublicServantListView, PublicServantDetailView, PublicServantUpdateView, PublicServantDeleteView

urlpatterns = [
    path('create/', PublicServantCreateView.as_view(), name='publicservant_create'),
    path('', PublicServantListView.as_view(), name='publicservant_list'),
    re_path(r'^(?P<pk>\d+)/$', PublicServantDetailView.as_view(), name='publicservant_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', PublicServantUpdateView.as_view(), name='publicservant_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', PublicServantDeleteView.as_view(), name='publicservant_delete')
]