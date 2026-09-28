# 3. Le model entreprie 
## 3.1 Reponse aux questions de  Specialisation 
### 1. Identification sans ambiguité d'une entreprise

Une contrainte d'unicité  sur le couple (nom ,ville) de l'entreprise.
Une chaîne comme Ecobank a une agence à Sokodé et une à Lomé , ces de agenges font juridiquement partie de la même entreprise mais etant donnée qu'on souaite qu'ils se trouvent dans de differents localité ils ont des contactes differents

### 2. Le type de champ pour l'adresse mail
 `EmailField()` car il empeche la saisie ou l'enregistrement de text qui ne sont pas des email,il garanditie que c'est bien un email . 


### 3. Le secteur d'activité : Texte libre ou liste imposée ?
* **texte libre :** 
 -Aujourd'hui il facilite l'enregistrement des données 
 -Dans 3 mois on peut avoit des fautes d'ortographe ce qui rend dificile recherche par secteurs d'activité,ou une difficulté a categorisé une entreprise.  
* **une liste de valeurs imposée:**
-Aujourd'hui il est un peut fatigant a implémenter,mais facilite la saisie les secteurs d'activités et permet d'evité les fautes.
-Dans 3 mois nos donnée enregistrer nous permetrons de facilement catégorisé les entreprise par secteurs d'activité et de facilité la recherche.

### 4. Interprétation de la dernière phrase du secrétariat
* **Décision :** Implémentation de la méthode magique `__str__(self)` renvoyant `f"{self.nom} ({self.ville})"`.
* **Pourquoi :** Le secrétariat veut identifier l'entreprise "tout de suite, sans avoir à cliquer". En surchargeant cette méthode, Django affiche ce texte explicite à la place de l'identifiant opaque par défaut (`Entreprise object (1)`).
  
## Rendu
### 1.
```bash

uv sync

```
Ce qui garantie que ce sera exatement le meme c'est le fait que les fichiers `pyproject.toml` et `uv.lock`
contiennent toutes les dependences du projet

### 2.
le fichier models.py

### 3.
le titre du message d'erreur et les fichiers conserné par l'erreur
