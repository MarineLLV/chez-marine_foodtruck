from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name