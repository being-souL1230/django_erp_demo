from django.urls import path
from .views import (
    home, add_student, update_student, delete_student, register, 
    faculty_list, add_faculty, delete_faculty, student_detail, 
    upload_assignment, assignment_list, student_login, student_logout, 
    student_dashboard, faculty_login, faculty_logout, faculty_dashboard
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Student Auth
    path('student-login/', student_login, name='student_login'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('student-logout/', student_logout, name='student_logout'),

    # Faculty Auth
    path('faculty-login/', faculty_login, name='faculty_login'),
    path('faculty-dashboard/', faculty_dashboard, name='faculty_dashboard'),
    path('faculty-logout/', faculty_logout, name='faculty_logout'),

    # Student CRUD
    path('', home, name='home'),
    path('add/', add_student, name='add_student'),
    path('update/<int:pk>/', update_student, name='update_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),
    path('register/', register, name='register'),
    path('student/<int:pk>/', student_detail, name='student_detail'),

    # Faculty CRUD
    path('faculty/', faculty_list, name='faculty_list'),
    path('add-faculty/', add_faculty, name='add_faculty'),
    path('delete-faculty/<int:pk>/', delete_faculty, name='delete_faculty'),

    # Assignments
    path('upload-assignment/', upload_assignment, name='upload_assignment'),
    path('assignments/', assignment_list, name='assignment_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)