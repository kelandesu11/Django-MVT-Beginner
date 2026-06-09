from rest_framework import serializers
from .models import Department
from courses.models import Course


class DepartmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "course_code",
            "credits",
            "level",
            "is_active",
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "code",
            "description",
            "building_name",
            "created_at",
            "course_count",
        ]

    def get_course_count(self, obj):
        return obj.courses.count()


class DepartmentDetailSerializer(serializers.ModelSerializer):
    courses = DepartmentCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "code",
            "description",
            "building_name",
            "created_at",
            "courses",
        ]