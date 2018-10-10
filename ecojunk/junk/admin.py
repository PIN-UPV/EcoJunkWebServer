from django.contrib import admin
from .models import JunkPoint
from django.contrib.auth import admin as auth_admin
# Register your models here.


@admin.register(JunkPoint)
class UserAdmin(auth_admin.UserAdmin):

    fieldsets = ("location", "type", "contract")
    list_display = ["location", "type", "contract"]
    search_fields = ["location"]
