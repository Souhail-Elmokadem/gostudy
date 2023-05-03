from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Enseignant(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    nom = models.CharField(max_length=30)
    datenaissence = models.DateField()
    photo = models.ImageField(upload_to='prof/img/pdp/%y')
    datecreation = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom