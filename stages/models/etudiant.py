from django.db import models
from .personne import Personne 
from .competence import Competence



class Etudiant(Personne):


    matricule = models.CharField(max_length=120)
    promotion = models.PositiveSmallIntegerField(
        help_text='2026'
    )
    competences = models.ManyToManyField(
        Competence,related_name="etudiants"
    )

    class Meta(Personne.Meta):

        verbose_name = "etudiant"
        verbose_name_plural = 'etudiants'

    

