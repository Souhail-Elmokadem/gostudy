from django.shortcuts import render
from courses.models import categorie,course
from etudiant.models import etudiant,Enrollement
from django.db.models import Count
import os,openai
# openai key


# Create your views here.
def index(request):
    
   
    
    # et = etudiant.objects.all().get(id=request.user.id)
    m ={
        # 'etd':etudiant.objects.values('Enrollement').annotate(Tcours=Count('etudiant')),
        'cats':categorie.objects.annotate(Tcours=Count('course')),
        'cours':course.objects.all().order_by('datecreation')[:3],
        'coursR':course.objects.all().order_by('-datecreation')[:6]
        # 'coursEnrolled':Enrollement.objects.all().filter(etudiant=et)
        
    }
    return render(request,"home/index.html",m)


api_key = "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"

def ai(request):
    msg = ""
    if request.method == "POST":
        openai.api_key = api_key
        u_input = request.POST.get('user_input')
        prompt = u_input
        try:
            response = openai.Completion.create(
                model = "gpt-3.5-turbo-0301",
                prompt = prompt,
                max_tokens = 256,
                temperature = 0.5,
                )
        except Exception as e:
            msg = e
    return render(request,'home/ai.html',{'e':msg})