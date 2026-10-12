from django.db import connection, reset_queries
from stages.models import Offre
reset_queries()
for offre in Offre.objects.select_related("entreprise").prefetch_related("competences"):
    offre.entreprise.nom
    list(offre.competences.all())
    len(connection.queries)