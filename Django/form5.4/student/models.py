from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, choices=[
        ('ASIR', 'ASIR'),
        ('DAW', 'DAW'),
        ('DAM', 'DAM')
    ])

    def __str__(self):
        return f"{self.name} ({self.degree})"
