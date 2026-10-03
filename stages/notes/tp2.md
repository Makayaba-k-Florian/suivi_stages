# tp2
## 1. Un modèle par fichier
**a.**  Django repond :`No changes detected`
Djando identifie un modele par le nom de la classe et non le chemin.
consernant les migrations Django ne suis pas non plus les chemin mais plutot la classe elle meme (les changement qui y on été éffectués).
## 2.2 Ce qu’elle ne dit pas
 -Personne doit avoir sa propre table. 
 -le tuteur appartient aussi a une  entreprise.
 -Une candidature ne peut-elle pas donner lieu à deux stages , Un stage peut exister sans candidature ,
la relation entre candidature et stage le permet , au niveau de la base  elle-même.
 -« Jamais deux fois à la même offre » : pour le garantir il faut etablire des relation qui l'interdise , la base donne le verifie.
 -Pour la promotion une entier est plus adapter car il est facile de fait des calcules et des statistics
 -Pour le statut d’une candidature : du texte libre serait une mauvaise idée car cella renedrais les recherche et les classement compliqué,Une liste fermée est une meilleur car sela resoudrait les problemes lier au text libre .
 -Pour cella on va utiliser PROTECT pour evitez la suppression des n-uplet qui y sont relier.

 ## Artbitrage
 Une Personne a les information commune entre ,etudiant,enseignant,tuteur.
 Une entreprise peut avoir plusieurs employés ,  mais nous ne prenons que les employés tuteurs.
 Une entreprise peut envoient des offres.
 Une offre est relier a des competences.
 Un etudiant a plusieurs competences et il peut candidater a plusieurs offres differents.
 une candidature retenue devient un stage.
 Un ou plusieurs etudiants peuvent faire un meme stage.
 un stage est encadrer par un enseigant et un tuteur(employé maitre de stage).
 on ne peut pas supprimer une entreprise qui a publié des offres ou qui a des tuteurs ou qui a acceuili un stage, pour ne pas effacer leur historique.
  on ne peut pas supprimer un etudiant ou un enseigant ou un tuteur  ayant intervenu dans un stage un stage, pour ne pas effacer leur historique.
 on ne peut pas supprimer une offre ayant fait l'objet d'une candidature , pour ne pas effacer leur historique.
     