from django.urls import path,include
from.import views

urlpatterns = [

    path('',views.index),
    path('studentregistration/',views.student_reg.as_view()),
    path('studentsview/',views.viewstud_reg.as_view()),
    path('studloginid/<int:login_id>',views.studentlogin.as_view()),
    path('studupdate/<int:login_id>',views.studentupdate.as_view()),
    path('studdelete/<int:login_id>',views.studentdelete.as_view()),
    

    path('login/',views.login_view.as_view()),
    path('faculty/',views.faculty_reg.as_view()),
    path('facultyview/',views.viewfaculty_reg.as_view()),
    path('facultyloginid/<int:login_id>',views.facultylogin.as_view()),
    path('facultyupdate/<int:login_id>',views.facultyupdate.as_view()),
    path('facultydelete/<int:login_id>',views.facultydelete.as_view()),

    path('HODregistration/',views.HOD_reg.as_view()),
    path('HODview/',views.viewHOD_reg.as_view()),
    path('HODloginid/<int:login_id>',views.HODlogin.as_view()),
    path('HODupdate/<int:login_id>',views.HODupdate.as_view()),
    path('HODdelete/<int:login_id>',views.HODdelete.as_view()),



    path('departmentregistration/',views.department_reg.as_view()),
    path('departmentview/',views.viewdepartment_reg.as_view()),
    path('departmentupdate/<int:id>',views.Departmentupdate.as_view()),
    path('departmentdelete/<int:id>',views.Departmentdelete.as_view()),

    path('semesterregistration/',views.semester_reg.as_view()),
    path('semesterview/',views.viewsemester.as_view()),




    

]
