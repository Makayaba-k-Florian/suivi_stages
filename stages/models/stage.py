from django.db import models
from .etudiant import Etudiant 
from .entreprise import Entreprise
from .enseignant_referent import EnseignantReferent
from .tuteur_entreprise import TuteurEntreprise 
from .candidature import Candidature








class Stage(models.Model):


    sujet = models.CharField()

    etudiants = models.ManyToManyField(
        Etudiant,related_name='stages'
    )

    entreprise = models.ForeignKey(
        Entreprise,on_delete=models.PROTECT,
        related_name="stages"
    )
    enseigant = models.ForeignKey(
        EnseignantReferent,on_delete=models.PROTECT,
        related_name="stages"
    )
    tuteur = models.ForeignKey(
        TuteurEntreprise,on_delete=models.PROTECT,
        related_name="stages"
    )
    candidature = models.OneToOneField(
        Candidature,on_delete=models.PROTECT,
        related_name='stage',
        null=True
    )



    class Meta():

        verbose_name = "stage"
        verbose_name_plural = 'stages'

    

