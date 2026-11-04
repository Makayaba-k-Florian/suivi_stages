from django import forms

from .models import Offre, Candidature


class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = (
            "titre",
            "date_debut",
            "date_fin",
            "description",
            "nb_places",
            "competences",
        )


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ("date_depot",)
        widgets = {
            "date_depot": forms.SelectDateWidget(years=range(2020, 2031)),
                   }

class StatutCandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ("statut",)
        
