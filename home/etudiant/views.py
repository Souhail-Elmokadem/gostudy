from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,authenticate
from etudiant.decorators import notLoginUsers
from django.contrib.auth.models import User,Group
from etudiant.models import etudiant,Enrollement
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
@notLoginUsers
def etudiant_login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            messages.success(request,user.username + ' login success !')
            return redirect('home')
        else:
            messages.info(request,' login error !')
    return render(request,'auth/etudiant/login.html')

@notLoginUsers
def etudiant_register(request):
        if request.method == "POST":
              form = etudLoginForm(request.POST)
              if form.is_valid():
                    user = form.save()
                    group = Group.objects.get(name="etudiant")
                    user.groups.add(group)
                    etudiant(id=user.id,user=user,nom=user.username,datenaissence=request.POST.get('datenaissence'),NiveauEtudiant=request.POST.get('NiveauEtudiant')).save()
                    messages.success(request,'Register successful')
                    return redirect('etudiant_login')
        else:
              form = etudLoginForm()
        return render(request,'auth/etudiant/register.html',{'f':form})

@login_required(login_url='etudiant_login')
def profile(request):
     et = etudiant.objects.all().get(user=request.user)
     enr = Enrollement.objects.all().filter(etudiant=et).count()
     crs = Enrollement.objects.all().filter(etudiant=et)
     l = {
          'etd':et,
          'nbE':enr,
          'crs':crs
     }
     return render(request,'etudiant/index.html',l)

def updateProfile(request):
    et = etudiant.objects.all().get(user=request.user)
    if request.method == "POST":
       form =  etudForm(request.POST,request.FILES,instance=et)
       if form.is_valid():
            form.save()
    l = {
          'etd':et,
          
     }
    return render(request,'etudiant/update.html',l)

class PasswordChangeView(PasswordChangeView):
     form_class = MyChangeFormPassword
     success_url = reverse_lazy("profile")
     
# def updatePassword(request):
#      et = etudiant.objects.all().get(user=request.user)
     
#      l = {
#         'etd':et,  
#     }
#      return render(request,'etudiant/updatePassword.html',l)