from django.db import models
import datetime

# Create your models here.


class Medicament(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    instruction = models.TextField()
    type_medicament = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='medicaments/', null=True, blank=True)

    def __str__(self):
        return f'Name: {self.name}, quantity: {self.quantity}, expiration_date: {self.expiration_date}'
