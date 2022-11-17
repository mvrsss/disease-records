from discover.models import Discover
from django import forms

class DiscoverForm(forms.ModelForm):
    class Meta:
        model = Discover
        fields = "__all__"