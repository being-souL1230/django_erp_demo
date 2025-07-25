from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='default@example.com')
    password = models.CharField(max_length=100, default='default_password')  # Add default value

    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='default_password') 
    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.name} - {self.file.name}'