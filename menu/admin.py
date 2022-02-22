from django.contrib import admin
from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'vegetarian', 'price')
    search_fields = ['name']

admin.site.register(Food, FoodAdmin)