from django.db import models
from django.contrib.auth.models import User
from courses.models import course
# Create your models here.

class etudiant(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=30)
    datenaissence = models.DateField()
    photo = models.ImageField(upload_to='etudiant/img/pdp/%y')
    levels = (
        ('1er annee','1er annee'),('2eme annee','2eme annee'),
        ('3eme annee','3eme annee'),('4eme annee','4eme annee'),
        ('5eme annee','5eme annee'),('6eme annee','6eme annee'),
    )
    NiveauEtudiant = models.CharField(max_length=50,choices=levels)
    datecreation = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(course,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    