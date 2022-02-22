from django.shortcuts import render
from django.http import HttpResponse
from .models import Food


# /menu
def index(request):
    foods = Food.objects.all()
    foods_names = [food.name for food in foods]
    foods_names_str = ", ".join(foods_names)
    return HttpResponse("Les galettes : " + foods_names_str)