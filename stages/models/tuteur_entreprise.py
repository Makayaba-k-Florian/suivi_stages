from django.db import models
from .personne import Personne
from .entreprise import Entreprise



class TuteurEntreprise(Personne):

    entreprise = models.ForeignKey(
        Entreprise,on_delete=models.PROTECT,
        related_name="tuteurs"
    )

    class Meta(Personne.Meta):

        pass
    
    
