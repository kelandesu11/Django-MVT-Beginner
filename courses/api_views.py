from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filterset_fields = ["department", "is_active"]
    search_fields = ["title", "course_code", "description"]
    ordering_fields = ["course_code", "title", "credits", "level"]