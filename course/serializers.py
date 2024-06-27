# course/serializers.py

from rest_framework import serializers
from .models import CourseType, Course, Session, Instructor, Assistant, Enrollment


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    assistants = AssistantSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
