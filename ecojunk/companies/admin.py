from django.contrib import admin
from .models import Contract
from .models import Company


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "promoted", ]
    search_fields = ["name", ]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ["company", "end_date", ]
