from django.contrib import admin
from .models import Enrollment, AuditLog


admin.site.register(Enrollment)
admin.site.register(AuditLog)