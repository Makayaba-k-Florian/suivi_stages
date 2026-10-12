from django.db import connection, reset_queries
from stages.models import Offre
reset_queries()
for offre in Offre.objects.all():
    offre.entreprise.nom
    #list(offre.competences.all())
    len(connection.queries)