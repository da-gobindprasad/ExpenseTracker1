from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=100)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
