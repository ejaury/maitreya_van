Required apps 
=============
* django-grappelli 2.3.7

* Python Imaging Library 1.1.7

* django-tagging 0.3.1

* django-photologue 2.2:
  Follow instructions here to setup: http://code.google.com/p/django-photologue/wiki/ReadMe

* django-treemenus 0.8.6

* python-dateutil 1.5 - required by django-schedule


Included libraries/apps
=======================
* django-schedule 1.0 RC-2

* django-contact-form 4 (jezdez fork): https://github.com/jezdez/django-contact-form

* django-tinymce 3.3.8


Initial Deployment Setup
========================
1. Create a calendar with slug 'temple'
#. Add a menu called 'Main', or define menu name in settings.py (MAIN_MENU_NAME)
#. Add 1st-level treemenu items (eventually database fixtures should be created for this) to the menu

Database Creation
=================
Create a db with UTF-8:
CREATE DATABASE maitreya_van CHARACTER SET utf8;

Troubleshootings
================
Changing table encoding to UTF-8:
alter table <table-name> convert to character set utf8 collate utf8_general_ci;
