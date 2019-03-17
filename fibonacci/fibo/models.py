from django.db import models

# Create your models here.

class NFibo(models.Model):
    number = models.PositiveIntegerField(primary_key = True)
    fibo = models.CharField(max_length = 300, null = True)
    def __str__(self):
        return str(self.number) + ' --> ' + self.fibo
