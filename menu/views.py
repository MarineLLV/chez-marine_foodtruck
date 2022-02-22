from django.shortcuts import render
from django.http import HttpResponse
from .models import Food


# /menu
def index(request):
    foods = Food.objects.all()
    foods_names_and_prices = [food.name + " : " + str(food.price) + "€" for food in foods]
    foods_names_and_prices_str = ", ".join(foods_names_and_prices)
    return HttpResponse("Les galettes : " + foods_names_and_prices_str)