from django.shortcuts import render
from courses.models import categorie,course
from etudiant.models import etudiant,Enrollement
from django.db.models import Count
# Create your views here.
def index(request):
    
   
    
    # et = etudiant.objects.all().get(id=request.user.id)
    m ={
        'cats':categorie.objects.annotate(Tcours=Count('course')),
        'cours':course.objects.all().order_by('datecreation')[:3],
        # 'coursEnrolled':Enrollement.objects.all().filter(etudiant=et)
        
    }
    return render(request,"home/index.html",m)


