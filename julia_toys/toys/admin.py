from django.contrib import admin

from toys.models import Toy, ToyImage


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    """Класс админки для игрушек."""

    list_display = [
        'id',
        'name',
    ]


@admin.register(ToyImage)
class ToyImageAdmin(admin.ModelAdmin):
    """Класс админки для игрушек."""

    list_display = [
        'id',
        'toy',
    ]
