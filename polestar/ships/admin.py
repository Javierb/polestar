from django.contrib import admin
from .models import Ship, Position

@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    pass

@admin.register(Position)
class ShipAdmin(admin.ModelAdmin):
    pass