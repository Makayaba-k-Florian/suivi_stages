import random
from datetime import date, timedelta

from django.conf.locale import en


from stages.models import (
    Entreprise, Etudiant, TuteurEntreprise, EnseignantReferent, 
    Offre, Competence, Candidature, Stage
)

print("Nettoyage")
Stage.objects.all().delete()
Candidature.objects.all().delete()
Offre.objects.all().delete()
Etudiant.objects.all().delete()
TuteurEntreprise.objects.all().delete()
EnseignantReferent.objects.all().delete()
Entreprise.objects.all().delete()
Competence.objects.all().delete()



print("Début du peuplement de la base de données...")

c_python = Competence.objects.create(libelle="django")
c_sql = Competence.objects.create(libelle="SQL / PostgreSQL")
c_js = Competence.objects.create(libelle="JavaScript / React")
c_devops = Competence.objects.create(libelle="Docker & DevOps")
c_agile = Competence.objects.create(libelle="Méthodes Agiles")
toutes_competences = [c_python, c_sql, c_js, c_devops, c_agile]

ent_1 = Entreprise.objects.create(nom="Sokodé Tech Solutions", ville="Sokodé", secteur="Informatique",contact="sts@gmail.com",)
ent_2 = Entreprise.objects.create(nom="Centrale Numérique Togo", ville="Sokodé", secteur="Télécoms",contact="sn@gmail.com")
ent_3 = Entreprise.objects.create(nom="Lomé Data Systems", ville="Lomé", secteur="Banque & Assurance",contact="lds@gmail.com")

tut_1 = TuteurEntreprise.objects.create(nom="TRAORE", prenom="Ali", sexe="M",date_naissance=date.today()-timedelta(days=100),entreprise=ent_1)
tut_2 = TuteurEntreprise.objects.create(nom="KOFFI", prenom="Abla", sexe="F",date_naissance=date.today()-timedelta(days=100),entreprise=ent_2)


#enseignants
ens_1 = EnseignantReferent.objects.create(nom="AMEDEE", prenom="Jean", sexe="M",date_naissance=date.today()-timedelta(days=100))
ens_2 = EnseignantReferent.objects.create(nom="OUADJA", prenom="Marie", sexe="F",date_naissance=date.today()-timedelta(days=100))

#etudiants
et_1 = Etudiant.objects.create(matricule="MAT2026001", nom="DIALLO", prenom="Mamadou", sexe="M",date_naissance=date.today()-timedelta(days=100), promotion="2026")
et_2 = Etudiant.objects.create(matricule="MAT2026002", nom="ADANLE", prenom="Essi", sexe="F",date_naissance=date.today()-timedelta(days=100), promotion="2026")
et_3 = Etudiant.objects.create(matricule="MAT2026003", nom="BOUKARI", prenom="Yao", sexe="M",date_naissance=date.today()-timedelta(days=100), promotion="2026")
et_4 = Etudiant.objects.create(matricule="MAT2026004", nom="AYEVA", prenom="Fousséna", sexe="F",date_naissance=date.today()-timedelta(days=100), promotion="2026")
et_5 = Etudiant.objects.create(matricule="MAT2026005", nom="GADO", prenom="Abdou", sexe="M",date_naissance=date.today()-timedelta(days=100), promotion="2026")

#competences atribution
et_1.competences.add(c_python, c_sql)
et_2.competences.add(c_js, c_agile)
et_3.competences.add(c_python, c_devops)
et_4.competences.add(c_sql, c_js)
et_5.competences.add(c_devops, c_agile)


off_1 = Offre.objects.create(titre="Développeur Backend Django",date_debut=date.today() + timedelta(days=10),date_fin=date.today() + timedelta(days=100), description="Stage sur Sokodé pour concevoir une API REST.",nb_places=2,entreprise=ent_1)
off_1.competences.add(c_python, c_sql)

off_2 = Offre.objects.create(titre="Administrateur Système & Cloud",date_debut=date.today() + timedelta(days=10),date_fin=date.today() + timedelta(days=109), description="Mission de déploiement et d'automatisation à Sokodé.",nb_places=2,entreprise=ent_1)
off_2.competences.add(c_devops, c_sql)

off_3 = Offre.objects.create(titre="Intégrateur Front-end Senior",date_debut=date.today() + timedelta(days=10),date_fin=date.today() + timedelta(days=180), description="Refonte d'une application bancaire basée à Lomé.",nb_places=2,entreprise=ent_1)
off_3.competences.add(c_js, c_agile)


cand_1 = Candidature.objects.create(date_depot=date.today() - timedelta(days=10), statut="déposée", etudiants=et_1, offre=off_1)
cand_2 = Candidature.objects.create(date_depot=date.today() - timedelta(days=8), statut="refuseé", etudiants=et_3, offre=off_2)
cand_3 = Candidature.objects.create(date_depot=date.today() - timedelta(days=5), statut="retenue", etudiants=et_4, offre=off_1)
cand_4 = Candidature.objects.create(date_depot=date.today() - timedelta(days=4), statut="En déposée", etudiants=et_2, offre=off_3)
cand_5 = Candidature.objects.create(date_depot=date.today() - timedelta(days=2), statut="En refuseé", etudiants=et_5, offre=off_2)
cand_6 = Candidature.objects.create(date_depot=date.today() - timedelta(days=1), statut="retenue", etudiants=et_1, offre=off_3)

#stage
stage_1 = Stage.objects.create(sujet="Développement de l'API de gestion locale - Sokodé Tech",
                               enseignant=ens_1,tuteur=tut_1,entreprise=ent_1,candidature=cand_3)
stage_1.etudiants.add(et_4)

stage_2 = Stage.objects.create(sujet="Mise en production de l'infrastructure Cloud - Centrale Numérique",
                               enseignant=ens_2,tuteur=tut_2,entreprise=ent_2,candidature=cand_6)
stage_1.etudiants.add(et_1)


