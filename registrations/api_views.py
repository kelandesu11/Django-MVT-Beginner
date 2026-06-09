from django.db import transaction
from rest_framework import viewsets
from .models import Enrollment, AuditLog
from .serializers import EnrollmentSerializer, AuditLogSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    filterset_fields = ["student", "course", "status"]

    search_fields = [
        "student__full_name",
        "student__student_number",
        "course__course_code",
    ]

    ordering_fields = ["enrolled_at"]

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save()

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

    filterset_fields = ["action", "model_name"]
    ordering_fields = ["created_at"]