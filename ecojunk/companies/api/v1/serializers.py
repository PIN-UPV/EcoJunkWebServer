from rest_framework.serializers import ModelSerializer

from ecojunk.companies.models import Company, Contract


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ("name", "promoted")


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ("company", "end_date")
