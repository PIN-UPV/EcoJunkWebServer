from django.contrib.gis import admin

from ecojunk.junk.models import Deal, JunkPoint, JunkPointType, Trash, TrashType


@admin.register(JunkPoint)
class JunkPointAdmin(admin.ModelAdmin):
    list_display = ("location", "contract")
    search_fields = ("location",)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("created_date", "customer", "rider", "junk_point", "accepted_date")
    search_fields = ("junk_point", "created_date")


@admin.register(Trash)
class TrashAdmin(admin.ModelAdmin):
    list_display = ("deal", "name", "description", "type")
    search_fields = ("name", "description")


@admin.register(TrashType)
class TrashTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(JunkPointType)
class JunkPointTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
