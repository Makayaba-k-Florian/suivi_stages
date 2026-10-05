from django.db import models
from .etudiant import Etudiant 
from .competence import Competence 
from .entreprise import Entreprise








class Offre(models.Model):


    titre = models.CharField()
    description = models.CharField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_places = models.PositiveSmallIntegerField()
    competences = models.ManyToManyField(
        Competence,related_name="offres"
    )
    entreprise = models.ForeignKey(
        Entreprise,on_delete=models.PROTECT,
        related_name="offres"
    )


    class Meta():

        verbose_name = "offre"
        verbose_name_plural = 'offres'

    

