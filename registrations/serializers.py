from rest_framework import serializers
from .models import Enrollment, AuditLog


class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source="student.full_name",
        read_only=True
    )

    course_title = serializers.CharField(
        source="course.title",
        read_only=True
    )

    course_code = serializers.CharField(
        source="course.course_code",
        read_only=True
    )

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "student_name",
            "course",
            "course_title",
            "course_code",
            "status",
            "enrolled_at",
        ]

    def validate(self, data):
        student = data.get(
            "student",
            getattr(self.instance, "student", None)
        )

        course = data.get(
            "course",
            getattr(self.instance, "course", None)
        )

        if not course.is_active:
            raise serializers.ValidationError(
                "Cannot enroll in an inactive course."
            )

        queryset = Enrollment.objects.filter(
            student=student,
            course=course
        )

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Student is already enrolled in this course."
            )

        return data

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = [
            "id",
            "action",
            "model_name",
            "object_id",
            "message",
            "created_at",
        ]

        read_only_fields = fields