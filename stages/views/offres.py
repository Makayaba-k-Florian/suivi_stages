from django.shortcuts import get_object_or_404, redirect, render

from ..models import Offre, Entreprise, Competence

from django.http import HttpResponse
from ..forms import OffreForm

# Create your views here.


def liste_offres(request):
    offres = Offre.objects.select_related("entreprise").prefetch_related("competences")
    return render(request, "stages/liste_offres.html", {"offres": offres})


def detail_offre(request, id_offre: int):
    offre = get_object_or_404(
        Offre.objects.select_related("entreprise").prefetch_related(
            "candidatures", "competences","candidatures__etudiant"
        ),
        id=id_offre,
    )

    return render(request, "stages/detail_offre.html", {"offre": offre})


def publier_offre(request, entreprise_id: int):
    entreprise = get_object_or_404(Entreprise, pk=entreprise_id)
    competences = Competence.objects.all()

    if request.method == "POST":
        form = OffreForm(request.POST)
        if form.is_valid():
            offre = form.save(commit=False)
            offre.entreprise = entreprise
            offre.save()
            form.save_m2m()
            return redirect("stages:detail_offre", id_offre=offre.id)
    else:
        form = OffreForm()

    return render(
        request,
        "stages/publier_offre.html",
        {"entreprise": entreprise, "competences": competences, "form": form},
    )
