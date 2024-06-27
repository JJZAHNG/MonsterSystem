# course/urls.py

from django.urls import path
from .views import CourseTypeListView, CourseListView, CourseDetailView, SessionListView, SessionDetailView, EnrollmentListView

urlpatterns = [
    path('course-types/', CourseTypeListView.as_view(), name='course_type_list'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('sessions/', SessionListView.as_view(), name='session_list'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
]
