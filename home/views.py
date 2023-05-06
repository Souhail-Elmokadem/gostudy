from django.shortcuts import render
from courses.models import categorie,course
from django.db.models import Count
# Create your views here.
def index(request):
    m ={
        'cats':categorie.objects.annotate(Tcours=Count('course')),
        'cours':course.objects.all().order_by('datecreation')[:3],
        
    }
    return render(request,"home/index.html",m)

