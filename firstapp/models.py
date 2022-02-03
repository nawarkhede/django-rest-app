from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_length=10, decimal_places=3, max_digits=30)

    def __str__(self):
        return f"{self.name} {self.salary}"


class Organization(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.address}"


class Student(models.Model):
    name = models.CharField(max_length=30)
    std = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.std}"


class City(models.Model):
    name = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.pincode}"


class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=20)
    rating = models.CharField(max_length=10)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.rating} {self.author}"


