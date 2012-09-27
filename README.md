skilleton : templates pour Django
================================

skilleton contient deux templates :

  1. `project_template` est utilisé pour initialiser un nouveau projet
  2. `app_template` sert à ajouter une application au sein d'un projet

**Caractéristiques :**

  * j'essaye de mettre le maximum de bonnes pratiques dans ces templates
  * le fichier settings est divisé entre le fichier de developpement et le fichier de production
  * les paramètres de production sont prévus pour tourner sur [alwaysdata](http://alwaysdata.com) donc via fcgi
  * le projet utilise [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/), [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) et [South](http://south.aeracode.org/)
  * le template du projet est minimaliste tandis que l'application contient des ébauches de formulaires/modèles/vues pouvant servir de pense-bête


Initialisation d'un projet Django
=================================

Utilisation
-----------

    $ django-admin.py startproject $PROJECT_NAME --template=skilleton/project_template --name=.secret_key


Après l'initialisation
----------------------

  1. créer le virtualenv avec les programmes requis (alternative pour alwaysdata)
  2. initialiser la base de données
  3. virer l'internationalisation si ce n'est pas nécessaire

**Commandes :**
    
    mkvirtualenv -r requirements.txt $PROJECT_VENV
    # alternative pour éviter les désagréments en déployant sur alwaysdata
    mkvirtualenv -r requirements.txt -p /usr/bin/python2.6 $PROJECT_VENV
    
    # Bonne pratique : utiliser django-admin.py plutôt que manage.py
    add2virtualenv $(pwd)'/$PROJECT_NAME'
    echo "export DJANGO_SETTINGS_MODULE=$PROJECT_NAME.settings.dev" >> $VIRTUAL_ENV/bin/postactivate
    echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
    
    django-admin.py syncdb


Ajout d'une application
=======================

  1. créer l'application dans le répertoire `/apps` en utilisant le template
  2. l'ajouter à `INSTALLED_APPS` dans `$PROJECT_NAME/settings/default.py`
  3. ajouter l'application à south

**Commandes :**

    cd apps
    django-admin.py startapp $APP_NAME --template=skilleton/app_template
    # ajout à INSTALLED_APPS
    django-admin.py schemamigration $APP_NAME --initial
    django-admin.py migrate


To-do list
==========
  * Tout traduire en français
  * Ajouter le support de [Haystack](http://haystacksearch.org)
