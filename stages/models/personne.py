from django.db import models

# Create your models here.

class Personne(models.Model):


    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    sexe = models.TextChoices("F","M")
    date_naissance = models.DateField(auto_now=False)
    email = models.EmailField()

    class Meta:
        ordering = ["nom"]
        verbose_name = "personne"
        verbose_name_plural = 'personnes'
        abstract = True
    

