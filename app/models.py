from django.db import models
from django.contrib.auth.models import User

class Sujet (models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom 

class Serie (models.Model):
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom
    
class Examen(models.Model):
    titre = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='fichier')
    image = models.ImageField(upload_to='', default='mg/IMG_20240627_164802_770_70oVlNG.jpg')
    sujet = models.ForeignKey(Sujet, on_delete=models.CASCADE, related_name='sujets')
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='series')
    annee = models.IntegerField(default=0)
    def __str__(self):
       return f" {self.titre}.{self.sujet}.{self.serie}.{self.annee} "
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sujet = models.ForeignKey(Sujet, on_delete=models.CASCADE, related_name='categorie', null=True)
    image = models.ImageField(upload_to='profil_picture')
    bio = models.CharField(max_length=1000)
   