from django.contrib import admin
from .models import Ship, Position
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    fields = ('name', 'imo_number')
    list_display = ('ship','created', 'updated',)

    def ship(self, obj):
        return str(obj)


@admin.register(Position)
class ShipAdmin(admin.ModelAdmin):
    list_display = ('ship', 'date', 'latitude', 'longitude')
