from django import forms
from .models import User

class UserForm(forms.ModelForm):
    sso_options = forms.MultipleChoiceField(
        choices=[
            ('mail', 'Mail'), 
            ('payroll', 'Payroll'), 
            ('selfservice', 'Selfservice')
        ],
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = User
        fields = ['user_name', 'password', 'city', 'web_server', 'rol', 'sso_options']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña', 'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'placeholder': 'Ingrese su usuario', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Ingrese su ciudad', 'class': 'form-control'}),
            'web_server': forms.Select(attrs={'class': 'form-control'}),
            'rol': forms.RadioSelect(),
        }
