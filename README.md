# Plateforme de Financement Participatif (Crowdfunding)

## À propos de la plateforme
Notre application web de crowdfunding est une solution complète développée avec Django, permettant aux utilisateurs de participer activement au financement de projets innovants. Elle offre une expérience utilisateur fluide et sécurisée pour la création et le soutien de projets.

## Fonctionnalités principales

### Gestion des utilisateurs
- Création de compte et authentification sécurisée
- Personnalisation du profil utilisateur
- Gestion des informations personnelles avec possibilité de modification et suppression
- Interface intuitive pour la gestion des projets

### Gestion des projets
- Création détaillée de projets de financement
- Tableau de bord pour le suivi des projets
- Système de modification et suppression des projets
- Visualisation complète des informations des projets

### Interaction avec les projets
- Système de dons sécurisé
- Mécanisme d'évaluation des projets
- Fonction de signalement pour la modération
- Système de commentaires interactif

## Architecture technique

### Technologies utilisées
- Framework Django (Python)
- Base de données SQLite3
- Interface utilisateur : HTML5, CSS3, JavaScript
- Framework CSS : Bootstrap
- Gestion des dépendances : pip

## Guide d'installation

### Prérequis
- Python 3.x ou version supérieure
- Gestionnaire de paquets pip
- Environnement virtuel (virtualenv)
- Git pour le clonage du projet

### Étapes d'installation

1. Clonage du référentiel
```bash
git clone [URL_DU_PROJET]
cd [NOM_DU_PROJET]
```

2. Configuration de l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Pour Linux/Mac
venv\Scripts\activate     # Pour Windows
```

3. Installation des dépendances
```bash
pip install -r requirements.txt
```

4. Configuration de la base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Collection des fichiers statiques
```bash
python manage.py collectstatic
```

6. Lancement du serveur de développement
```bash
python manage.py runserver
```

## Configuration du projet

### Structure des fichiers
```
project/
├── apps/                      # Dossier principal des applications
│   ├── authentication/        # Gestion de l'authentification
│   ├── home/                  # Application principale
│   ├── static/                # Fichiers statiques (CSS, JS, images)
│   ├── templates/             # Templates HTML
│   ├── __init__.py           # Initialisation du package Python
│   ├── config.py             # Configuration des applications
│   └── context_processors.py  # Processeurs de contexte Django
├── core/                      # Configuration centrale du projet
├── db.sqlite3                 # Base de données SQLite
├── gunicorn-cfg.py           # Configuration du serveur Gunicorn
├── manage.py                  # Script de gestion Django
├── package.json              # Dépendances Node.js
├── requirements.txt          # Dépendances Python
└── README.md                 # Documentation du projet
```

### Configuration de la base de données
Modifiez le fichier settings.py pour configurer votre base de données :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Maintenance et support

### Mises à jour
- Vérifier régulièrement les mises à jour de sécurité
- Mettre à jour les dépendances via pip
- Sauvegarder la base de données avant toute mise à jour majeure

### Résolution des problèmes courants
En cas d'erreurs lors de l'installation ou de l'exécution, vérifier :
- La version de Python
- L'activation de l'environnement virtuel
- La configuration de la base de données
- Les permissions des fichiers

## Contribution
Pour contribuer au projet :
1. Créer une branche pour vos modifications
2. Suivre les conventions de code du projet
3. Tester vos modifications
4. Soumettre une pull request
## Équipe de Développement

HAMMALE MOURAD  
MALIKA GAREH  
DOUAE FARCHAKHI  
FRIK AYA  
HABBANI MOHAMMED  
HILAL AYOUB  
CHAIMAE HAMMACH  
