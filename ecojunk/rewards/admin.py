from django.contrib import admin

from ecojunk.rewards.models import Badge, Mission


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description", "level")


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
