#!/usr/bin/env python
# vim: et ts=4 sw=4


# inherit everything from rapidsms, as default
# (this is optional. you can provide your own.)
from rapidsms.djangoproject.settings import *


# then add your django settings:

DEBUG = True

DATABASE_ENGINE = "sqlite3"
DATABASE_NAME = "db.sqlite3"

INSTALLED_APPS = (
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    'django.contrib.humanize',
    "rapidsms.contrib.djangoadmin",
    "django.contrib.admin",
    "rapidsms",
    "rapidsms.contrib.handlers",
    "rapidsms.contrib.echo",
    "rtwilio",
)

TABS = [
    ('rapidsms.views.dashboard', 'Dashboard'),
]

INSTALLED_BACKENDS = {
    "twilio": {"ENGINE": "rtwilio.backend"},
    "message_tester" : {"ENGINE": "rapidsms.backends.bucket" } 
}

TEST_RUNNER = "django_nose.run_tests"
