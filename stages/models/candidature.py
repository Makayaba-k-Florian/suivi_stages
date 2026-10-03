from django.db import models
from .etudiant import Etudiant 
from .offre import Offre 





class Candidature(models.Model):

    class Statut(models.TextChoices):
        DEPOSEE = "déposée"
        REFUSEE = 'refuseé'
        RETENU = "retenue"
        
    date_depot = models.DateField()
    statut = models.CharField(choices=Statut)
    etudiants = models.ManyToManyField(
        Etudiant,related_name="candidatures"
    )
    offre = models.ForeignKey(
        Offre,on_delete=models.PROTECT,
        related_name='candidatures'
    )

    class Meta():

        verbose_name = "candidature"
        verbose_name_plural = 'candidatures'

    

