# course/admin.py

from django.contrib import admin
from .models import CourseType, Course, Session, Instructor, Assistant, Enrollment


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']


@admin.register(Assistant)
class AssistantAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'course_type', 'start_date', 'end_date', 'capacity', 'instructor']
    filter_horizontal = ('assistants',)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['course', 'session_date', 'start_time', 'end_time', 'location']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enrolled_date']
