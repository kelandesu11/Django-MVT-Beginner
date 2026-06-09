from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filterset_fields = ["is_active", "enrollment_year"]
    search_fields = ["full_name", "email", "student_number"]
    ordering_fields = ["full_name", "enrollment_year", "created_at"]