from specialize.models import Specialize
from django import forms

class SpecializeForm(forms.ModelForm):
    class Meta:
        model = Specialize
        fields = "__all__"