from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_length=10, decimal_places=3, max_digits=30)

    def __str__(self):
        return f'{self.name} {self.salary}'