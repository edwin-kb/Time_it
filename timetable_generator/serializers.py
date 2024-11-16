from rest_framework import serializers
from .models import Login
from .models import Student
from .models import Faculty,HOD,Department,Semesters
class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Student
        fields = '__all__'
         
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
     class Meta:
        model = Faculty
        fields = '__all__'

class HODSerializer(serializers.ModelSerializer):
     class Meta:
        model = HOD
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Department
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):
     class Meta:
        model = Semesters
        fields = '__all__'

