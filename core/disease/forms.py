from disease.models import Disease
from django import forms

class DiseaseForm(forms.ModelForm):

    class Meta:
        model = Disease
        fields = "__all__"