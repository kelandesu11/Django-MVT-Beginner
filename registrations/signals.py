from django.db.models.signals import post_save
from django.dispatch import receiver

from students.models import Student
from courses.models import Course
from .models import Enrollment, AuditLog


@receiver(post_save, sender=Student)
def create_student_audit_log(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="student_created",
            model_name="Student",
            object_id=instance.id,
            message=f"Student {instance.student_number} - {instance.full_name} was created."
        )


@receiver(post_save, sender=Course)
def create_course_audit_log(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="course_created",
            model_name="Course",
            object_id=instance.id,
            message=f"Course {instance.course_code} - {instance.title} was created."
        )


@receiver(post_save, sender=Enrollment)
def create_enrollment_audit_log(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="enrollment_created",
            model_name="Enrollment",
            object_id=instance.id,
            message=f"Student {instance.student.student_number} enrolled in {instance.course.course_code}."
        )