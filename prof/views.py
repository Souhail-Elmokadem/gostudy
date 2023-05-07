from django.shortcuts import render,redirect
from .models import Enseignant
from .forms import profLoginForm
from courses.models import course,categorie,tag
from etudiant.models import Enrollement
from django.contrib import messages
from django.db.models import Sum
from .forms import courseForm
# Create your views here.

def getstarted(request):
    return render(request,'prof/getstarted.html')


def registerprof(request):
    form = profLoginForm()
    if request.method == "POST":
        form = profLoginForm(request.POST)
        if form.is_valid():
            user=form.save()
            Enseignant(id=user.id,user=user,nom=user.username,datenaissence=request.POST.get('datenaissence')).save()
            messages.success(request,user.username, ' created !')
            return redirect('etudiant_login')
    return render(request,'prof/registerprof.html',{'u':form})

def dashboardprof(request):
    m = {
        'countcours':course.objects.all().filter(Enseignant=request.user.id).count(),
        'courstudents':Enrollement.objects.all().filter(cours__Enseignant=request.user.id).count(),
        'hours':course.objects.filter(Enseignant=request.user.id).aggregate(h=Sum('duration')),
        'pdp':Enseignant.objects.all().get(user=request.user)
     }
    
    return render(request,'prof/dashboard.html',m)

def dashboardcourses(request):
    m = {
    'pdp':Enseignant.objects.all().get(user=request.user),
    'cours':course.objects.all().filter(Enseignant=request.user.id)
    }
    return render(request,'prof/courses.html',m)

def createcourse(request):
    form = courseForm()
    ens = Enseignant.objects.all().get(user=request.user)
    if request.method == "POST":
        form = courseForm(request.POST,request.FILES,instance=course(Enseignant=ens))
        if form.is_valid():
            form.save()
            
    m = {
        'pdp':Enseignant.objects.all().get(user=request.user),
        'categories':categorie.objects.all(),
        'tags':tag.objects.all(),
        'f':form
    }
    

    return render(request,'prof/createcourse.html',m)