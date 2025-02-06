from django import forms 

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={"required": "Your name must not be empty!", "max_length":"Please enter a shorter name!"},
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'form-control'}))

    password = forms.CharField(
        label="Password",
                widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-control'})
)
    
    city = forms.CharField(
        label="City of employment",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'form-control'}))
    webserver = forms.ChoiceField(
        label="Web Server",
        choices=[('apache', 'Apache'), ('nginx', 'Nginx'), ('iis', 'IIS')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    role = forms.ChoiceField(
        label="Please specify your role",
        choices=[('admin', 'Admin'), ('engineer', 'Engineer'), ('manager', 'Manager'), ('guest', 'Guest')],
        widget=forms.RadioSelect()
    )
    sso_options = forms.MultipleChoiceField(
        label="Single Sign-on to the following",
        choices=[('mail', 'Mail'), ('payroll', 'Payroll'), ('selfservice', 'Self-service')],
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
