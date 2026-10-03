from django.db import models



class Competence(models.Model):

    class Libelle(models.TextChoices):
        FASTAPI = 'fastapi'
        PYTHON = 'python'
        DJANGO = 'django'
        LARAVEL = 'laravel'
        
        JAVA = "JAVA", "Java"
        C = "C", "C"
        PHP = "PHP", "PHP"
        

        HTML_CSS = "HTML_CSS", "HTML / CSS"
        JAVASCRIPT = "JAVASCRIPT", "JavaScript"
        

        SQL = "SQL", "SQL"
        POSTGRESQL = "POSTGRESQL", "PostgreSQL"
        MYSQL = "MYSQL", "MySQL"
        

        GIT = "GIT", "Git & GitHub"
        LINUX = "LINUX", "Linux / Systèmes"
        RESEAUX = "RESEAUX", "Bases des réseaux (TCP/IP)"
        

        ALGORITHMIQUE = "ALGORITHMIQUE", "Algorithmique & Structures de données"

    libelle = models.CharField(max_length=120,choices=Libelle)
   

    class Meta:

        verbose_name = "competence"
        verbose_name_plural = 'competences'

    
    
