from django.urls import path, re_path
from countries.views import CountryCreateView, CountryListView, CountryDetailView, CountryUpdateView, CountryDeleteView

urlpatterns = [
    path('create/', CountryCreateView.as_view(), name='country_create'),
    path('', CountryListView.as_view(), name='country_list'),
    re_path(r'^(?P<pk>\d+)/$', CountryDetailView.as_view(), name='country_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', CountryUpdateView.as_view(), name='country_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', CountryDeleteView.as_view(), name='country_delete')
]