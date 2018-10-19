from django.contrib import admin

from ecojunk.companies.models import Company, Contract


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "promoted")
    search_fields = ("name",)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("company", "end_date")
