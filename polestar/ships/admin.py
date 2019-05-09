from django.contrib import admin
from .models import Ship

@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    pass