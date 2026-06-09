from rest_framework.routers import DefaultRouter

from departments.api_views import DepartmentViewSet
from courses.api_views import CourseViewSet
from students.api_views import StudentViewSet
from registrations.api_views import EnrollmentViewSet, AuditLogViewSet


router = DefaultRouter()

router.register("departments", DepartmentViewSet)
router.register("courses", CourseViewSet)
router.register("students", StudentViewSet)
router.register("enrollments", EnrollmentViewSet)
router.register("audit-logs", AuditLogViewSet)

urlpatterns = router.urls