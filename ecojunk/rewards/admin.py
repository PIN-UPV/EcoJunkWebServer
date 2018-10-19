from django.contrib import admin
from .models import Mission
from .models import Badge
# Register your models here.


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "level", ]
    search_fields = ["name", "description", "level", ]


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ["name", "description", ]
    search_fields = ["name", "description", ]

