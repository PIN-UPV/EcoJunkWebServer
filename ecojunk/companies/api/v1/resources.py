from rest_framework.viewsets import ReadOnlyModelViewSet

from ecojunk.companies.api.v1.serializers import CompanySerializer, ContractSerializer
from ecojunk.companies.models import Company, Contract
from ecojunk.core.api.permissions import NoDeletes, NoUpdates
from rest_framework.permissions import IsAuthenticated


class CompanyResource(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, NoDeletes, NoUpdates]


class ContractResource(ReadOnlyModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, NoDeletes, NoUpdates]
