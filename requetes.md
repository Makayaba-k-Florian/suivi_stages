# 5.2 Six Requêtes 

### 1. Les offres des entreprises situées à Sokodé
```python
Offre.objects.filter(entreprise__ville="Sokodé")
```

### 2. Les étudiants qui possèdent la compétence « Django »
```python
Etudiant.objects.filter(competences__libelle="django")
```

### 3. Les candidatures d’un étudiant donné, en partant de l’objet étudiant
```python
etudiant = Etudiant.objects.get(nom="DIALLO")

candidatures_etudiant = etudiant.candidatures.all()

print(candidatures_etudiant)
```

### 4. Le nombre de candidatures retenues, sans charger les candidatures en mémoire
```python
nb_candidatures_retenues = Candidature.objects.filter(statut="retenue").count()
print(nb_candidatures_retenues)

```

### 5. Les stages dont l’offre vient d’une entreprise de Sokodé
```python
Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé")
```

### 6. Les offres qui demandent au moins une compétence que possède un étudiant donné
```python
etudiant = Etudiant.objects.get(nom="DIALLO")

offres_compatibles = Offre.objects.filter(
    competences__in=etudiant.competences.all()
).distinct()

print(offres_compatibles)

```