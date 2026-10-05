from django.db import models

# Create your models here.

class Personne(models.Model):

    class Sexe(models.TextChoices):
        FEMME = "F"
        HOMME = "M"
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    sexe = models.CharField(choices=Sexe,null=True)
    date_naissance = models.DateField()
    email = models.EmailField()

    class Meta:
        ordering = ["nom"]
        verbose_name = "personne"
        verbose_name_plural = 'personnes'
        abstract = True
    

