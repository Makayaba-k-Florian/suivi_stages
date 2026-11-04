


from django.shortcuts import get_object_or_404, redirect, render

from stages.models import candidature, entreprise

from ..models import Offre, Entreprise, Competence,Etudiant,Candidature

from django.http import HttpResponse, request
from ..forms import CandidatureForm,StatutCandidatureForm


def candidater_offre(request,offre_id,etudiant_id):
    etudiant = get_object_or_404(Etudiant,pk=etudiant_id)
    offre = get_object_or_404(Offre,pk=offre_id)
    try:
        candidature = Candidature.objects.get(etudiant=etudiant,offre=offre)
    except Candidature.DoesNotExist:
        candidature = None
    if candidature:
        return redirect("stages:detail_offre", id_offre=offre.id)

    if request.method == "POST":
        form = CandidatureForm(request.POST)
        if form.is_valid():
            candidature = form.save(commit=False)
            candidature.etudiant = etudiant
            candidature.offre = offre
            candidature.save()
            return redirect("stages:detail_offre", id_offre=offre.id)
    else:
        form = CandidatureForm()
    return render(
        request,
        "stages/candidature.html",
        {"etudiant": etudiant, "offre": offre,"form":form},
    )

def changer_statut(request, candidature_id):
    candidature1 = get_object_or_404(Candidature, pk=candidature_id)
    if request.method != "POST":
        return redirect("stages:detail_offre", id_offre=candidature1.offre.id)
    print(request.POST)
    form = StatutCandidatureForm(request.POST,instance=candidature1)
    print(form)
    if form.is_valid():
        form.save()
        
    return redirect("stages:detail_offre", id_offre=candidature1.offre.id)
