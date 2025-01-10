from django import forms

class activosForms(forms.Form):
    code_activo = forms.IntegerField()
    name_activo = forms.CharField(max_length=200)
    category_activo = forms.CharField(max_length=200, required=False)
    num_serie = forms.IntegerField()
    marc_activo = forms.CharField(max_length=50)
    area_activo = forms.CharField(max_length=100)
    stade_activo = forms.CharField(max_length=200)
    value_activo = forms.IntegerField()
    last_maintenance = forms.DateTimeField(required=False)
    guarantee_activo_time = forms.CharField(max_length=200)