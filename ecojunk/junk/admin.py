from django.contrib.gis import admin

from .models import JunkPoint


@admin.register(JunkPoint)
class JunkPointAdmin(admin.ModelAdmin):
    list_display = ("location", "type", "contract")
    search_fields = ("location",)
