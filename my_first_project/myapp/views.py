from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Faculty, Assignment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
@login_required
def home(request):
    query = request.GET.get('q')

    if query:
        student_list = Student.objects.filter(name__icontains=query)
    else:
        student_list = Student.objects.all()
    
    paginator = Paginator(student_list, 5)  # Show 5 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'myapp/home.html', {'students' : students})


@login_required
def faculty_list(request):
    faculty = Faculty.objects.all()
    return render(request, 'myapp/faculty_list.html', {'faculty': faculty})

@login_required
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'myapp/student_detail.html', {'student': student})

def faculty_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            faculty = Faculty.objects.get(email=email, password=password)
            request.session['faculty_id'] = faculty.id
            return redirect('faculty_dashboard')
        except Faculty.DoesNotExist:
            messages.error(request, 'Invalid faculty credentials')
    return render(request, 'myapp/faculty_login.html')

def faculty_dashboard(request):
    if 'faculty_id' not in request.session:
        return redirect('faculty_login')
    faculty = Faculty.objects.get(id=request.session['faculty_id'])
    return render(request, 'myapp/faculty_dashboard.html', {'faculty': faculty})

@login_required
def add_faculty(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dept = request.POST['department']
        password = request.POST['password']
        Faculty.objects.create(name=name, email=email, phone=phone, department=dept, password=password)
        return redirect('faculty_list')
    return render(request, 'myapp/add_faculty.html')

@login_required
def delete_faculty(request, pk):
    f = Faculty.objects.get(id=pk)
    f.delete()
    return redirect('faculty_list')

def faculty_logout(request):
    if 'faculty_id' in request.session:
        del request.session['faculty_id']
    return redirect('faculty_login')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'myapp/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'myapp/register.html', {'form': form}) 

def student_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            student = Student.objects.get(email=email, password=password)
            request.session['student_id'] = student.id
            return redirect('student_dashboard')
        except Student.DoesNotExist:
            messages.error(request, 'Invalid student credentials')
    return render(request, 'myapp/student_login.html')


def student_logout(request):
    if 'student_id' in request.session:
        del request.session['student_id']
    return redirect('student_login')

def student_dashboard(request):
    if 'student_id' not in request.session:
        return redirect('student_login')
    student = Student.objects.get(id=request.session['student_id'])
    return render(request, 'myapp/student_dashboard.html', {'student': student})
@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = StudentForm()
        return render(request, 'myapp/add_student.html', {'form': form})
    
@login_required
def upload_assignment(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST['student']
        file = request.FILES['file']
        student = Student.objects.get(id=student_id)
        Assignment.objects.create(student=student, file=file)
        return redirect('assignment_list')
    return render(request, 'myapp/upload_assignment.html', {'students': students})

@login_required
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'myapp/assignment_list.html', {'assignments': assignments})

@login_required
def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'myapp/update_student.html', {'form': form})
@login_required
def  delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'myapp/delete_student.html', {'student': student})