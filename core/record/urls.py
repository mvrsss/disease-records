from django.urls import path, re_path
from record.views import RecordCreateView, RecordListView, RecordDetailView, RecordUpdateView, RecordDeleteView

urlpatterns = [
    path('create/', RecordCreateView.as_view(), name='record_create'),
    path('', RecordListView.as_view(), name='record_list'),
    re_path(r'^(?P<pk>\d+)/$', RecordDetailView.as_view(), name='record_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', RecordUpdateView.as_view(), name='record_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', RecordDeleteView.as_view(), name='record_delete')
]