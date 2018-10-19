from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.fields import GeometryField

from ecojunk.companies.models import Contract, Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ("name", "promoted")


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ("company", "end_date")
