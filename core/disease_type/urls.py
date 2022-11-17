from django.urls import path, re_path
from disease_type.views import DiseaseTypeCreateView, DiseaseTypeListView, DiseaseTypeDetailView, DiseaseTypeUpdateView, DiseaseTypeDeleteView

urlpatterns = [
    path('create/', DiseaseTypeCreateView.as_view(), name='disease_type_create'),
    path('', DiseaseTypeListView.as_view(), name='disease_type_list'),
    re_path(r'^(?P<pk>\d+)/$', DiseaseTypeDetailView.as_view(), name='disease_type_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', DiseaseTypeUpdateView.as_view(), name='disease_type_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', DiseaseTypeDeleteView.as_view(), name='disease_type_delete')
]