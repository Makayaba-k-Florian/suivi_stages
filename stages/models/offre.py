from django.db import models
from .etudiant import Etudiant 
from .competence import Competence 
from .entreprise import Entreprise

from django.core.exceptions import ValidationError







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

    def clean(self):
        if self.date_debut >= self.date_fin:
            raise ValidationError(
                {
                    "date_debut":"la date de debut doit etre inferieur a la date de fin"
                }
            )
        if self.nb_places < 1:
                raise ValidationError(
                    {
                        "nb_places":"le nombres de places doit etre supperieur a 0"
                    }
                )

    class Meta():

        verbose_name = "offre"
        verbose_name_plural = 'offres'

    

