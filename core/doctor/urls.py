from django.urls import path, re_path
from doctor.views import DoctorCreateView, DoctorListView, DoctorDetailView, DoctorUpdateView, DoctorDeleteView

urlpatterns = [
    path('create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('', DoctorListView.as_view(), name='doctor_list'),
    re_path(r'^(?P<pk>\d+)/$', DoctorDetailView.as_view(), name='doctor_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', DoctorUpdateView.as_view(), name='doctor_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', DoctorDeleteView.as_view(), name='doctor_delete')
]