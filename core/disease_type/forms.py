from disease_type.models import DiseaseType
from django import forms

class DiseaseTypeForm(forms.ModelForm):

    class Meta:
        model = DiseaseType
        fields = "__all__"