prswb
=====

Scrum vu des petites tranchées

[![Build Status](https://secure.travis-ci.org/prswb/prswb.png?branch=master)](http://travis-ci.org/prswb/prswb)

Installation
============

```
$ git clone https://github.com/prswb/prswb.git
$ cd prswb
$ virtualenv --no-site-packages `pwd`/.env
$ source .env/bin/activate
$ pip install -r requirements-dev.txt
```

To launch a local dev webserver instance:

```
$ python manage.py runserver
Validating models...

0 errors found
Django version 1.4.1, using settings 'uxperiment.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Head to `http://127.0.0.1:8000/`, profit.
