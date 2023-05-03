from django.shortcuts import render
from .models import *
from django.db.models import Count
# Create your views here.

def CoursesList(request):
    categories = {
         'cat1':categorie.objects.all()[0],
         'cat2':categorie.objects.all()[1],
         'cat3':categorie.objects.all()[2],
         'cat4':categorie.objects.all()[3],
         'cours':course.objects.all(),
         'nbetudInscrit':course.objects.annotate(number_of_etudiants=Count('etudiant')),
         
        }
    
    return render(request,'courses/courseslist.html',categories)