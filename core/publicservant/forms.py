from publicservant.models import PublicServant
from django import forms

class PublicServantForm(forms.ModelForm):
    class Meta:
        model = PublicServant
        fields = "__all__"