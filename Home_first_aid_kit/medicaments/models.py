from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Medicament(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    instruction = models.TextField()
    type_medicament = models.CharField(max_length=100)
    category = models.TextField()
    image = models.ImageField(null=True, blank=True)
    medicament_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.name}, quantity: {self.quantity}, expiration_date: {self.expiration_date}'
