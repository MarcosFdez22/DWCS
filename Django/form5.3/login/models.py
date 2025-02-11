from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    web_server = models.CharField(
        max_length=10,
        choices=[('apache', 'Apache'), ('nginx', 'Nginx'), ('iis', 'IIS')]
    )
    rol = models.CharField(
    max_length=10,
    choices=[('admin', 'Admin'), ('engineer', 'Engineer'), ('manager', 'Manager'), ('guest', 'Guest')],
    default='guest' 
)
    sso_options = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.user_name
