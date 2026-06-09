from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer, DepartmentDetailSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    search_fields = ["name", "code"]
    ordering_fields = ["name", "code"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DepartmentDetailSerializer

        return DepartmentSerializer