from django.shortcuts import render,redirect
from .models import *
from etudiant.models import Enrollement,etudiant
from django.db.models import Count
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from etudiant.models import etudiant
# Create your views here.

def CoursesList(request):
    categories = {
         'cours':course.objects.all().order_by('datecreation'),
        }
    return render(request,'courses/courseslist.html',categories)

def CoursesListS(request,pk):
    Coursecategories = {
         'cours':course.objects.all().order_by('datecreation').filter(categorie=pk),
        }
    return render(request,'courses/courseslist.html',Coursecategories)

@login_required(login_url='etudiant_login')
def coursedetails(request,pk):
    crs = course.objects.all().get(id=pk)
    try:
        qrs = Enrollement.objects.values('cours').annotate(Tet=Count('etudiant')).get(cours=pk)
        checkuser = Enrollement.objects.filter(etudiant=request.user.etudiant,cours=crs).first()
    except ObjectDoesNotExist:
        qrs = None
        checkuser=None
    m =  {
        'cours':course.objects.annotate(number_of_etudiants=Count('etudiant')).get(id=pk),
        # Find the Enrollement and group by the course:
        'enrs':qrs,
        'userEnrol':checkuser
        }
    return render(request,'courses/coursedetails.html',m)

@login_required(login_url='etudiant_login')
def EnrollCourse(request,pk):
    crs = course.objects.all().get(id=pk)
    form = Enrollement(cours=crs,etudiant=request.user.etudiant)
    if request.method == "POST":
        checkuser = Enrollement.objects.filter(etudiant=request.user.etudiant,cours=crs).first()
        if checkuser is None:
            form.save()
            messages.success(request,'Enrolled avec success')
            return redirect('ViewCourse',pk=pk)
        else:
            return redirect('home')
    return render(request,'courses/Enroll.html')

@login_required(login_url='etudiant_login')
def viewCourse(request,pk):
    et = etudiant.objects.all().get(id=request.user.id)
    crs = course.objects.all().get(id=pk)
    enr = Enrollement.objects.all().filter(etudiant=et)
    
        
    m={
        'enr':enr,
        'cours':crs,
        'ett':et,
    }
    return render(request,'courses/courseview.html',m)
