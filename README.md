# prswb <sup>[![Build Status](https://secure.travis-ci.org/prswb/prswb.png?branch=master)](http://travis-ci.org/prswb/prswb)</sup>

**Code related to the «[Scrum vu des petites tranchées](http://www.paris-web.fr/2012/conferences/scrum-vue-des-petites-tranchees.php)» talk to be given at [Paris-Web 2012](http://www.paris-web.fr/2012/).**

Installation
------------

Clone the project:

```
$ git clone https://github.com/prswb/prswb.git
$ cd prswb
```

Create a new [virtualenv](http://pypi.python.org/pypi/virtualenv) in `./.env` and enable it:

```
$ virtualenv --no-site-packages `pwd`/.env
$ source .env/bin/activate
```

Install dependencies:

```
$ pip install -r requirements-dev.txt
```

Configure the project (more informations on [settings management](#settings-management)):

```
$ echo 'DEBUG=True' > uxperiment/settings/local.py
$ echo 'export DJANGO_SETTINGS_MODULE=uxperiment.settings.local' >> .env/bin/postactivate
$ echo 'export unset DJANGO_SETTINGS_MODULE' >> .env/bin/postdeactivate
```

To launch a local dev webserver instance:

```
$ python manage.py runserver --settings=uxperiment.settings.local
Validating models...

0 errors found
Django version 1.4.1, using settings 'uxperiment.settings.local'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Head to `http://127.0.0.1:8000/`, profit.

Settings management
-------------------

This django project has a `settings/` directory having a setting module per environment:

    settings/
        |- base.py      # commong settings
        |- staging.py   # staging env for heroku
        |- test.py      # travis env
        |- local.py     # dev env

Le fichier `local.py` n’est pas versionné pour cette raison. Il est stocké dans un dossier privé et son accès doit être controlé et vérifié.

Custom settings should be stored in a `settings/local.py` module.

Deploying on Heroku
-------------------

The staging is hosted on [Heroku](http://heroku.com/) and reachable at
[http://aqueous-mountain-3105.herokuapp.com/](http://aqueous-mountain-3105.herokuapp.com/).

Your git user must have `push` privileges on the heroku repository. You must also provide your SSH public key to the admin account of the `uxperiment` project.

Once done, add this section to the `.git/config` of your local clone of the repo:

```
[remote "heroku"]
    url = git@heroku.com:aqueous-mountain-3105.git
    fetch = +refs/heads/*:refs/remotes/heroku/*
```

To push and deploy to heroku:

```
$ git push heroku master
```

After a push, Heroku will load the packages defined in the `requirements.txt` file. This file also contains packages for `postgres` and `gunicorn`.

At the end of the process, the `Procfile` will be used by Heroku to start the server.

To tell Heroku to use the staging settings module:

```
$ heroku config:set DJANGO_SETTINGS_MODULE=uxperiment.settings.staging
```

The `staging` settings module uses environment variables to configure the platform; to set them you have to use the `heroku config:add` command:

```
$ heroku config:add VARIABLE=VALUE
```

Travis-CI Test Environment
--------------------------

The `.travis.yml` file at the root of the repository contains the required configuration.
