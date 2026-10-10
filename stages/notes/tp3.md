# tp3
### 3. Une feuille de style
**a.** J'ai placé le fichier css dans static , car en django les fichiers static y sont placer pour faciliter
la gestion. <br>
**b.**
En production, pour des raisons de performance, on évite de surcharger le serveur Django avec les fichiers CSS/JS. On les dépose souvent sur un serveur externe (un CDN ou un "bucket" AWS S3).
Ecrire {% static 'stages/style.css' %} plutôt que /static/stages/style.css permet de rendre dynamiques l'endroi ou se trouve les fichiers statiques.
<br>

### 4. Compter les requêtes

uv run manage.py shell