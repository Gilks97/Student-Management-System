import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from student_management_app.models import CustomUser, staffs, Courses, Subjects, Students, FeedBackStudent, FeedBackStaffs, LeaveReportStudent, LeaveReportStaff, Attendance, AttendanceReport




def admin_home(request):
    return render(request, "hod_template/home_content.html")


def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")


def add_course(request):
    return render(request, "hod_template/add_course_template.html")


def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('/add_course')
    else:
        course = request.POST.get('course')
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request,"Course Added Successfully!")
            return redirect('/add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('/add_course')

def add_student(request):
    courses=Courses.objects.all()
    return render(request, 'hod_template/add_student_template.html', {"courses": courses})

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")
        try:
            user=CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)
            user.students.address=address
            course_obj=Courses.objects.get(id=course_id)
            user.students.course_id=course_obj
            start_date=datetime.datetime.strptime(session_start,'%d-%m-%y').strftime('%y-%m-%d')
            end_date=datetime.datetime.strptime(session_end,'%d-%m-%y').strftime('%y-%m-%d')
            
            user.students.session_start_year=start_date
            user.students.session_end_year=end_date
            user.students.gender=sex
            user.students.profile_pic=""
            user.save()
            messages.success(request, "Succesfully Added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to Add Student")
            return HttpResponseRedirect("/add_student")
        
        
def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'hod_template/manage_course_template.html', context)

def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    context = {
        "course": course,
        "id": course_id
    }
    return render(request, 'hod_template/edit_course_template.html', context)


def edit_course_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course')

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()

            messages.success(request, "Course Updated Successfully.")
            return redirect('/edit_course/'+course_id)

        except:
            messages.error(request, "Failed to Update Course.")
            return redirect('/edit_course/'+course_id)


def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    try:
        course.delete()
        messages.success(request, "Course Deleted Successfully.")
        return redirect('manage_course')
    except:
        messages.error(request, "Failed to Delete Course.")
        return redirect('manage_course')
    
def manage_student(request):
    students=Students.objects.all()
    return render(request, "hod_template/manage_student_template.html", {"students": students})

def manage_course(request):
    courses=Courses.objects.all()
    return render(request, "hod_template/manage_course_template.html", {"courses": courses})

