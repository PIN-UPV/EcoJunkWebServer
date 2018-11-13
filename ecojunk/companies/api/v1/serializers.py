from rest_framework.serializers import ModelSerializer

from ecojunk.companies.models import Company, Contract


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "name", "promoted")


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ("id", "company", "end_date")
