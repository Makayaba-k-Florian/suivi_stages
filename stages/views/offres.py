from django.shortcuts import render

from ..models import Offre

# Create your views here.

def liste_offres(request):
    offres = (
    Offre.objects
        .select_related("entreprise")
        .prefetch_related("competences")
    )
    return render(
        request,
        'stages/liste_offres.html',
        {"offres":offres}
    )
