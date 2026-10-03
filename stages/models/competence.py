from django.db import models



class Competence(models.Model):

    class Libelle(models.TextChoices):
        SQL = "SQL",'sql'
        FASTAPI = 'fastapi'
        PYTHON = 'python'
        DJANGO = 'django'
        LARAVEL = 'laravel'

    libelle = models.CharField(max_length=120,choices=Libelle)
   

    class Meta:

        verbose_name = "competence"
        verbose_name_plural = 'competences'

    
    
