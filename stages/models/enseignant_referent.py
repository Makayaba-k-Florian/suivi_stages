from django.db import models
from .personne import Personne


class EnseignantReferent(Personne):



    class Meta(Personne.Meta):

        pass
    
    
