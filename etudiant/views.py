from django.shortcuts import render,redirect
from .forms import etudLoginForm
from django.contrib import messages
from django.contrib.auth import login,authenticate
from etudiant.decorators import notLoginUsers
from django.contrib.auth.models import User,Group
from etudiant.models import etudiant
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


