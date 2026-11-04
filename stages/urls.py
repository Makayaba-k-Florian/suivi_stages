from django.urls import path
from . import views

app_name = "stages"

urlpatterns = [
    path('entreprises/',views.liste_entreprises,
         name= 'liste_entreprises'),
    
    path('',views.liste_offres,
             name= 'liste_offres'),
    
    path('/offres/<int:id_offre>/detail',views.detail_offre,
                 name= 'detail_offre'),
     path('/oentreprises/<int:id_entreprise>/detail',views.detail_entreprise,
                     name= 'detail_entreprise'),

     path('offres/publier/<int:entreprise_id>',
          views.publier_offre,
          name= 'publier_offre'),
     path('offres/<int:offre_id>/<int:etudiant_id>/candidater',
               views.candidater_offre,
               name= 'candidater_offre'),
     path('offres/<int:offre_id>/<int:etudiant_id>/candidater',
                    views.candidater_offre,
                    name= 'candidater_offre'),
     path('candidatures/<int:candidature_id>/changer_statut',
                    views.changer_statut,
                    name= 'changer_statut'),
]
