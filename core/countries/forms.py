from countries.models import Country
from django import forms

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = "__all__"