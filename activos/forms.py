from django import forms

class activosForms(forms.Form):
    code_activo = forms.IntegerField()
    name_activo = forms.CharField(max_length=200)
    category_activo = forms.CharField(max_length=200)
    num_serie = forms.CharField(max_length=10)
    marc_activo = forms.CharField(max_length=50)
    area_activo = forms.CharField(max_length=100)
    stade_activo = forms.CharField(max_length=200)
    value_activo = forms.DecimalField(max_digits=10, decimal_places=4, default=0.0, blank=True)
    date_add = forms.DateField()
    life_activo = forms.IntegerField(required=False, blank=True) 
    last_maintenance = forms.DateTimeField(required=False, blank=True)
    guarantee_activo = forms.CharField(max_length=40, required=False, blank=True)