from django import forms
from .models import register

class registerForm(forms.ModelForm):
    class Meta:
        model=register
        fields="__all__"
        labels={"name":"Full Name","gender":"Gender","email":"Email","contact":"Phone Number"}


from django import forms

class ZodiacSignForm(forms.Form):
    birth_date = forms.IntegerField(label="Day")
    birth_month = forms.IntegerField(label="Month")
    birth_year= forms.IntegerField(label="Year")




