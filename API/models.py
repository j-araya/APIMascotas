from django.db import models

SEX_CHOICES = [
    ('M','Male'),
    ('F','Female'),
]

class Pet(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    def __str__(self):
        return self.name
        

class Product(models.Model):

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    
        