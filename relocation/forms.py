from django import forms
from .models import Region, City


class HousingForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all().order_by('name'))
    city = forms.ModelChoiceField(queryset=City.objects.all().order_by('name'))

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('cities', None)
        super(HousingForm, self).__init__(*args, **kwargs)
        if qs:
            self.fields['city'].queryset = qs
            self.fields['city'].initial = qs[0].id
            self.fields['region'].initial = qs[0].region.id
