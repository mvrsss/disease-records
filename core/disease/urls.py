from django.urls import path, re_path
from disease.views import DiseaseCreateView, DiseaseListView, DiseaseDetailView, DiseaseUpdateView, DiseaseDeleteView

urlpatterns = [
    path('create/', DiseaseCreateView.as_view(), name='disease_create'),
    path('', DiseaseListView.as_view(), name='disease_list'),
    re_path(r'^(?P<pk>\d+)/$', DiseaseDetailView.as_view(), name='disease_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', DiseaseUpdateView.as_view(), name='disease_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', DiseaseDeleteView.as_view(), name='disease_delete')
]