from django.shortcuts import render,get_object_or_404
from ..models import Entreprise

# Create your views here.

def liste_entreprises(request):
    entreprises = (
    Entreprise.objects
        .prefetch_related("offres")
        .prefetch_related('competences')
    )
    return render(
        request,
        'stages/liste_entreprises.html',
        {"entreprises":entreprises,}
    )
    
def detail_entreprise(request,id_entreprise:int):
    entreprise = get_object_or_404(Entreprise,id=id_entreprise)
    return render(request,'stages/detail_entreprise.html',{"entreprise":entreprise})