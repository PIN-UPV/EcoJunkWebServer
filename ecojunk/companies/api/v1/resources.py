from rest_framework.viewsets import ReadOnlyModelViewSet

from ecojunk.companies.api.v1.serializers import CompanySerializer, ContractSerializer
from ecojunk.companies.models import Company, Contract
from ecojunk.core.api.permissions import NoDeletes, NoUpdates


class CompanyResource(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [NoDeletes, NoUpdates]


class ContractResource(ReadOnlyModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [NoDeletes, NoUpdates]