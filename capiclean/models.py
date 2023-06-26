from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Contact(models.Model):
    Name=models.CharField(max_length=100)
    Email = models.CharField(max_length=20)
    Phone =models.IntegerField()
    Message=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Carrer(models.Model):
    Designation=models.CharField(max_length=100)
    Salary=models.IntegerField()
    Qualification=models.CharField(max_length=200)

    def __str__(self):
        return self.Designation

class Apply(models.Model):
    Name=models.CharField(max_length=100)
    Email = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    Phone =models.IntegerField()
    CV=models.CharField(max_length=100)


    def __str__(self):
        return self.Name
