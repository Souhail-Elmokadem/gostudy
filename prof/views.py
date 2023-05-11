from django.shortcuts import render,redirect
from .models import Enseignant
from .forms import profLoginForm
from courses.models import course,categorie,tag
from etudiant.models import Enrollement
from django.contrib import messages
from django.db.models import Sum
from .forms import courseForm
from django.contrib.auth.decorators import login_required
from etudiant.decorators import allowedusers,notLoginUsers
from django.contrib.auth.models import Group
# Create your views here.

@notLoginUsers
@allowedusers(allowedGroups=['etudiant','admin'])
def getstarted(request):
    return render(request,'prof/getstarted.html')


@notLoginUsers
def registerprof(request):
    form = profLoginForm()
    if request.method == "POST":
        form = profLoginForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name="prof")
            user.groups.add(group)
            Enseignant(id=user.id,user=user,nom=user.username,datenaissence=request.POST.get('datenaissence')).save()
            messages.success(request,user.username, ' created !')
            return redirect('etudiant_login')
    return render(request,'prof/registerprof.html',{'u':form})

@login_required(login_url='etudiant_login')
@allowedusers(allowedGroups=['prof','admin'])
def dashboardprof(request):
    m = {
        'countcours':course.objects.all().filter(Enseignant=request.user.id).count(),
        'courstudents':Enrollement.objects.all().filter(cours__Enseignant=request.user.id).count(),
        'hours':course.objects.filter(Enseignant=request.user.id).aggregate(h=Sum('duration')),
        'pdp':Enseignant.objects.all().get(user=request.user)
     }
    
    return render(request,'prof/dashboard.html',m)

@login_required(login_url='etudiant_login')
@allowedusers(allowedGroups=['prof','admin'])
def dashboardcourses(request):
    m = {
    'pdp':Enseignant.objects.all().get(user=request.user),
    'cours':course.objects.all().filter(Enseignant=request.user.id)
    }
    return render(request,'prof/courses.html',m)

@login_required(login_url='etudiant_login')
@allowedusers(allowedGroups=['prof','admin'])
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

@login_required(login_url='etudiant_login')
@allowedusers(allowedGroups=['prof','admin'])
def editcourse(request,pk):
    crs = course.objects.all().filter(Enseignant=request.user.id).get(id=pk)
    if request.method == "POST":
        form = courseForm(request.POST,request.FILES,instance=crs)
        if form.is_valid():
            form.save()
            return redirect('dashboardcourses')
    m= {
        'pdp':Enseignant.objects.all().get(user=request.user),
        'cours':course.objects.all().filter(Enseignant=request.user.id).get(id=pk),
        'categories':categorie.objects.all(),
        'tags':tag.objects.all(),
        'f':courseForm(instance=crs)
    }
    return render(request,'prof/editcourse.html',m)

@login_required(login_url='etudiant_login')
@allowedusers(allowedGroups=['prof','admin'])
def deletecourse(request,pk):
    crs = course.objects.all().filter(Enseignant=request.user.id).get(id=pk)
    if request.method == "POST":
        crs.delete()
        return redirect('dashboardcourses')
    return render(request,'prof/deletecourse.html',{'cr':crs})