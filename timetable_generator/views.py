from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from.models import Student
from.models import Login,Faculty,HOD,Department,Semesters
from.serializers import LoginSerializer,FacultySerializer,HODSerializer,DepartmentSerializer,SemesterSerializer
from rest_framework import status


def index(request):
    return HttpResponse('qwertyuio')

# Create your views here
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class student_reg(GenericAPIView):
    def get_serializer_class(self):
        return StudentSerializer
    
    def post(self, request):
        login_id = ""
        name = request.data.get('name')
        email = request.data.get('email')
        mobile = request.data.get('mobile')
        password = request.data.get('password')
        department = request.data.get('department')
        role = 'student'

        if not name or not email or not mobile or not password or not department:
            return Response({'message': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Student.objects.filter(email=email).exists():
            return Response({'message': 'DUPLICATE EMAILS ARE NOT ALLOWED'}, status=status.HTTP_400_BAD_REQUEST)
        
        elif Student.objects.filter(mobile=mobile).exists():
            return Response({'message': 'Number already found'}, status=status.HTTP_400_BAD_REQUEST)
        
        login_serializer = LoginSerializer(data={'email': email, 'password': password, 'role': role})

        if login_serializer.is_valid():
            l = login_serializer.save()
            login_id = l.id
        else:
            return Response({'message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        student_serializer = StudentSerializer(data={
            'name': name,
            'email': email,
            'mobile': mobile,
            'password': password,
            'role': role,
            'login_id': login_id,
            'department': department
        })

        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class login_view(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
                email = request.data.get('email')
                password = request.data.get('password')

                logreg = Login.objects.filter(email=email, password=password)
                if(logreg.count()>0):
                    read_serializers = LoginSerializer(logreg, many = True)

                    for i in  read_serializers.data:
                        login_id = i['id']
                        role = i['role']

                        register_data = Student.objects.filter(login_id = login_id).values()
                        for i in register_data:
                            name = i['name']

                    return Response({'data' :read_serializers.data,'succes': 1,'message' : 'logged in succesfully'},status=status.HTTP_200_OK)
                
                else:
                    return Response({'message':'login failed'},status=status.HTTP_400_BAD_REQUEST,)
                
class faculty_reg(GenericAPIView):
    def get_serializer_class(self):
        return FacultySerializer
    
    def post(self, request):
        login_id = ""
        name = request.data.get('name')
        email = request.data.get('email')
        mobile = request.data.get('mobile')
        password = request.data.get('password')
        department = request.data.get('department')
        role = 'faculty'

        if not name or not email or not mobile or not password or not department:
            return Response({'message': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Faculty.objects.filter(email=email).exists():
            return Response({'message': 'DUPLICATE EMAILS ARE NOT ALLOWED'}, status=status.HTTP_400_BAD_REQUEST)
        
        elif Faculty.objects.filter(mobile=mobile).exists():
            return Response({'message': 'Number already found'}, status=status.HTTP_400_BAD_REQUEST)
        
        login_serializer = LoginSerializer(data={'email': email, 'password': password, 'role': role})

        if login_serializer.is_valid():
            l = login_serializer.save()
            login_id = l.id
        else:
            return Response({'message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        faculty_serializer = FacultySerializer(data={
            'name': name,
            'email': email,
            'mobile': mobile,
            'password': password,
            'role': role,
            'login_id': login_id,
            'department': department
        })

        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(faculty_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class HOD_reg(GenericAPIView):
    def get_serializer_class(self):
        return HODSerializer
    
    def post(self, request):
        login_id = ""
        name = request.data.get('name')
        email = request.data.get('email')
        mobile = request.data.get('mobile')
        password = request.data.get('password')
        department = request.data.get('department')
        role = 'HOD'

        if not name or not email or not mobile or not password or not department:
            return Response({'message': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if HOD.objects.filter(email=email).exists():
            return Response({'message': 'DUPLICATE EMAILS ARE NOT ALLOWED'}, status=status.HTTP_400_BAD_REQUEST)
        
        elif HOD.objects.filter(mobile=mobile).exists():
            return Response({'message': 'Number already found'}, status=status.HTTP_400_BAD_REQUEST)
        
        login_serializer = LoginSerializer(data={'email': email, 'password': password, 'role': role})

        if login_serializer.is_valid():
            l = login_serializer.save()
            login_id = l.id
        else:
            return Response({'message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        HOD_serializer = HODSerializer(data={
            'name': name,
            'email': email,
            'mobile': mobile,
            'password': password,
            'role': role,
            'login_id': login_id,
            'department': department
        })

        if HOD_serializer.is_valid():
            HOD_serializer.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(HOD_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class viewstud_reg(GenericAPIView):
    serializer_class = StudentSerializer
      
    
    def get(self, request):
        student = Student.objects.all()
        if student.count() > 0:
            serializer = StudentSerializer(student, many=True)
            return Response({'data' : serializer.data, 'message' : 'Data Get', 'success' : True},status=status.HTTP_200_OK)
        
        else:
            return Response({'data' : 'no data available'}, status=status.HTTP_400_BAD_REQUEST)
        
class viewfaculty_reg(GenericAPIView):
    serializer_class = FacultySerializer
      
    
    def get(self, request):
        Facultys = Faculty.objects.all()
        if Facultys.count() > 0:
            serializer = FacultySerializer(Facultys, many=True)
            return Response({'data' : serializer.data, 'message' : 'Data Get', 'success' : True},status=status.HTTP_200_OK)
        
        else:
            return Response({'data' : 'no data available'}, status=status.HTTP_400_BAD_REQUEST)
        
class viewHOD_reg(GenericAPIView):
    serializer_class = HODSerializer
      
    
    def get(self, request):
        hod = HOD.objects.all()
        if hod.count() > 0:
            serializer = HODSerializer(hod, many=True)
            return Response({'data' : serializer.data, 'message' : 'Data Get', 'success' : True},status=status.HTTP_200_OK)
        
        else:
            return Response({'data' : 'no data available'}, status=status.HTTP_400_BAD_REQUEST)
        
class studentlogin(GenericAPIView):
    serializer_class = StudentSerializer
      
    
    def get(self,request,login_id):
        student = Student.objects.get(login_id=login_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
        
class facultylogin(GenericAPIView):
    serializer_class = FacultySerializer
      
    
    def get(self,request,login_id):
        faculty = Faculty.objects.get(login_id=login_id)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)
    
class HODlogin(GenericAPIView):
    serializer_class = HODSerializer
      
    
    def get(self,request,login_id):
        hod = HOD.objects.get(login_id=login_id)
        serializer = HODSerializer(hod)
        return Response(serializer.data)
        

class studentupdate(GenericAPIView):
    serializer_class = StudentSerializer
      
    
    def put(self,request,login_id):
        student = Student.objects.get(login_id=login_id)
        serializer = StudentSerializer(instance=student , data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message' : 'user updated', 'success' : True},status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class facultyupdate(GenericAPIView):
    serializer_class = FacultySerializer
      
    
    def put(self,request,login_id):
        faculty = Faculty.objects.get(login_id=login_id)
        serializer = FacultySerializer(instance=faculty , data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message' : 'user updated', 'success' : True},status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class HODupdate(GenericAPIView):
    serializer_class = HODSerializer
      
    
    def put(self,request,login_id):
        hod = HOD.objects.get(login_id=login_id)
        serializer = HODSerializer(instance=hod , data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message' : 'user updated', 'success' : True},status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class studentdelete(GenericAPIView):
    serializer_class = StudentSerializer
      
    
    def delete(self,request,login_id):
        student = Student.objects.get(login_id=login_id)
        student.delete()
        return Response('deleted successfully')
    
class facultydelete(GenericAPIView):
    serializer_class = FacultySerializer
      
    
    def delete(self,request,login_id):
        faculty = Faculty.objects.get(login_id=login_id)
        faculty.delete()
        return Response('deleted successfully')
    
class HODdelete(GenericAPIView):
    serializer_class = HODSerializer
      
    
    def delete(self,request,login_id):
        hod = HOD.objects.get(login_id=login_id)
        hod.delete()
        return Response('deleted successfully')

class department_reg(GenericAPIView):
    def get_serializer_class(self):
        return DepartmentSerializer
    
    def post(self, request):
        
        depname = request.data.get('depname')
        dept_id = request.data.get('dept_id')
        
        
        department_serializer = DepartmentSerializer(data={
            'depname': depname,
            'dept_id': dept_id,
        })

        if department_serializer.is_valid():
            department_serializer.save()
            return Response({'message': 'Department Added Succesfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class viewdepartment_reg(GenericAPIView):
    serializer_class = DepartmentSerializer
      
    
    def get(self, request):
        department = Department.objects.all()
        if department.count() > 0:
            serializer = DepartmentSerializer(department,many=True)
            return Response({'data' : serializer.data, 'message' : 'Data Get', 'success' : True},status=status.HTTP_200_OK)
        
        else:
            return Response({'data' : 'no data available'}, status=status.HTTP_400_BAD_REQUEST)
        
class Departmentupdate(GenericAPIView):
    serializer_class = DepartmentSerializer
      
    
    def put(self,request,id):
        department = Department.objects.get(pk=id)
        serializer = DepartmentSerializer(instance=department , data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data, 'message' : 'user updated', 'success' : True},status=status.HTTP_200_OK)
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Departmentdelete(GenericAPIView):
    serializer_class = DepartmentSerializer
      
    
    def delete(self,request,id):
        department = Department.objects.get(pk=id)
        department.delete()
        return Response('deleted successfully')

class semester_reg(GenericAPIView):
    def get_serializer_class(self):
        return SemesterSerializer
    
    def post(self, request):
        
        semestername = request.data.get('semestername')
        
        
        
        semester_serializer = SemesterSerializer(data={
            'semestername': semestername,
            
        })

        if semester_serializer.is_valid():
            semester_serializer.save()
            return Response({'message': 'Semester Added Succesfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(semester_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class viewsemester(GenericAPIView):
    serializer_class = SemesterSerializer      
    
    def get(self, request):
        semester = Semesters.objects.all()
        if semester.count() > 0:
            serializer = SemesterSerializer(semester,many=True)
            return Response({'data' : serializer.data, 'message' : 'Data Get', 'success' : True},status=status.HTTP_200_OK)
        
        else:
            return Response({'data' : 'no data available'}, status=status.HTTP_400_BAD_REQUEST)