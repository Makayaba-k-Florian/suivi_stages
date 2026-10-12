from django.shortcuts import get_object_or_404, render

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

def detail_offre(request,id_offre:int):
    offre = get_object_or_404(Offre,id=id_offre)
    return render(request,'stages/detail_offre.html',{"offre":offre})