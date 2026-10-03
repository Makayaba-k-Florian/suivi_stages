from django.contrib import admin


# Register your models here.
from .models import Entreprise
from .models import Etudiant
from .models import TuteurEntreprise
from .models import Offre
from .models import EnseignantReferent
from .models import Competence
from .models import Stage
from .models import Candidature


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom","ville","secteur"]
    search_fields = ["nom",'ville']
    
    
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ["matricule","nom","prenom","sexe"
,"promotion"]
    search_fields = ["nom",'prenom']
    
@admin.register(TuteurEntreprise)
class TuteurEntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","sexe"]
    search_fields = ["nom",'prenom']

@admin.register(EnseignantReferent)
class EnseignantReferentAdmin(admin.ModelAdmin):
    list_display = ["nom","prenom","sexe"]
    search_fields = ["nom",'prenom']
    
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ["titre","description",]
    search_fields = ["titre",'competences']
    
    
@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ["libelle",]
    search_fields = ["libelle",]
    
@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ["date_depot","statut","etudiants","offre"]
    search_fields = ["etudiants",'date_depot']
    

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ["sujet",]
    search_fields = ["sujet",]
    