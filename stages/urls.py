from django.urls import path
from . import views

app_name = "stages"

urlpatterns = [
    path('entreprises/',views.liste_entreprises,
         name= 'liste_entreprises'),
    
    path('',views.liste_offres,
             name= 'liste_offres')
    
]
