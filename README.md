# UXperiment <sup>[![Build Status](https://secure.travis-ci.org/prswb/prswb.png?branch=master)](http://travis-ci.org/prswb/prswb)</sup>

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

To launch a local dev webserver instance:

```
$ export UXPERIMENT_ENV=dev
$ python manage.py runserver
Validating models...

0 errors found
Django version 1.4.1, using settings 'uxperiment.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Head to `http://127.0.0.1:8000/`, profit.

### Updating the codebase

After each `git pull`, you have to run the following commands:

```
$ pip install -r requirements-dev.txt
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py collectstatic
```

Working with Sass & Compass
---------------------------

Stylesheets are handled through [Compass](http://compass-style.org/).

To get started:

```
$ sudo gem install compass
$ cd generic/static
$ compass watch
>>> Compass is polling for changes. Press Ctrl-C to Stop.
```

Now you can edit the stylesheets in the `sass/` directory, related css files will
be compiled in the background.

Settings management
-------------------

This django project has a `settings/` directory having a setting module per environment:

    settings/
        |- base.py        # common shared settings
        |- dev.py         # dev settings
        |- production.py  # production settings (hosting platform yet to be determined)
        |- staging.py     # staging (hosted on heroku)
        |- test.py        # travis settings

Eventually, custom settings may be stored in a `settings/local.py` module.

The `UXPERIMENT_ENV` environment variable will set the specific settings module
to load. To run the local webserver against a given environment:

```
$ UXPERIMENT_ENV=test python manage.py runserver
```

If you intend to work always with a given environment within the project virtualenv:

```
$ echo 'export UXPERIMENT_ENV=dev' >> .env/bin/postactivate
$ echo 'export unset UXPERIMENT_ENV' >> .env/bin/postdeactivate
```

Deploying on Heroku
-------------------

The staging is hosted on [Heroku](http://heroku.com/) and reachable at
[http://aqueous-mountain-3105.herokuapp.com/](http://aqueous-mountain-3105.herokuapp.com/).

**Note:** You'll have to download and install the [Heroku Toolbelt](https://toolbelt.heroku.com/)
in order to manage some of the remote deployment procedures detailed below.

### Deploying with a push

Your git user must have `push` privileges on the heroku repository. You must also
provide your SSH public key to the admin account of the `uxperiment` project.

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

### Post push deployment

After a push, Heroku will load the packages defined in the `requirements.txt`
file. At the end of the process, the `Procfile` will be used by Heroku to start
the server.

Basically the `Procfile` will run these commands:

```
$ python manage.py migrate
$ python manage.py collectstatic --noinput
$ python manage.py run_gunicorn -b 0.0.0.0:$PORT
```

### Environment & settings

To tell Heroku to use the `staging` environment:

```
$ heroku config:set UXPERIMENT_ENV=staging
```

The `staging` settings module uses environment variables to configure the platform;
to set them you have to use the `heroku config:add` command:

```
$ heroku config:add VARIABLE=VALUE
```

Here are some of the settings required for the staging to work properly:

* `EMAIL_RECIPIENT`: The email address to receive notification emails sent from the platform
* `EMAIL_HOST_USER`: The email user account name to send the email from
* `EMAIL_HOST_PASSWORD`: The email user account password

### Heroku commands

You can always run django commands using the `heroku run` command, eg:

```
$ heroku run 'python manage.py migrate'
```

To tail the server logs:

```
$ heroku logs --tail
```

Travis-CI Test Environment
--------------------------

The `.travis.yml` file at the root of the repository contains the required configuration.

Code review
-----------

Somebody submitted a new pull-request, let's say: https://github.com/prswb/prswb/pull/24

This is a pull-request from `n1k0` on his `i18n-pages` branch. To retrieve the branch in order to test it:

```
$ git remote add n1k0 https://github.com/n1k0/prswb.git
$ git fetch n1k0 i18n-pages
From https://github.com/n1k0/prswb
 * branch            i18n-pages -> FETCH_HEAD
$ git checkout -b pr-24
Switched to a new branch 'pr-24'
$ git pull --rebase n1k0 i18n-pages
From https://github.com/n1k0/prswb
 * branch            i18n-pages -> FETCH_HEAD
```

Now you can launch tests, verify scenario and so on. To get back on master:

```
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 47 commits.
```

To sync from central repository:

```
$ git remote add upstream git://github.com/prswb/prswb.git
$ git pull upstream master
From git://github.com/prswb/prswb
 * branch            master     -> FETCH_HEAD
```
