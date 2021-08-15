Django To-do App
================

This is a simple Django To-Do App with PostgreSQL to demonstrate how to deploy Django application to Google Kubernetes Engine using Helm Charts and Github Action.

![todo App](https://raw.githubusercontent.com/NYARAS/helm-deploy-todo/main/todoApp.png)

How to install and run this project
-----------------------------------
Prerequisites
~~~~~~~~~~~~~
Make sure you have the following libraries installed before beginning:

- python3-dev
- git (`Configuring ssh`_)
- pip (`Installing pip`_)
- virtualenv & virtualenvwrapper `https://github.com/yyuu/pyenv <if using pyenv refer to this document>`_
- postgresql

Cloning from github
~~~~~~~~~~~~~~~~~~~
From your terminal go to the directory you want to clone the project into.

.. code:: bash

	$ cd path/to/your/directory

Clone the project.

.. code:: bash

	$ git clone git@github.com:NYARAS/helm-deploy-todo.git

Setting up the project's dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Navigate into the project directory from the terminal.

Setup the following dependencies.
 - `psycopg2`_ 
 - `setuptools`_ 
 - `python-dev`_ 
 - `python3-dev`_ 

.. _psycopg2: http://initd.org/psycopg/
.. _setuptools: https://pypi.python.org/pypi/setuptools
.. _python-dev: https://www.python.org/dev/
.. _python3-dev: https://www.python.org/dev/

.. code:: bash

	$ cd path/to/your/directory/erp-backend

Create a virtual environment to use for your project

.. code:: bash

  # Ignore this if you are not using virtualwrapper
  $ mkvirtualenv --python=/usr/bin/python3 env # env is the name of your virtual environment

Configure the virtualenv to prepare the test environment each time you activate it

.. code:: bash

  # Ignore this if you are not using virtualwrapper
  $ nano ~/{virtualenv_folder_path}/{env_name}/bin/postactivate
  # copy this --> run prepare_test_environment <-- to the opened file, then save

From your virtualenv do the following.

.. code:: bash

	(env)$ pip install -r requirements.txt # run this in a clean virtualenv
	(env)$ pip install -r requirements.txt
    (env)$ python manage.py makemigrations
	(env)$ python manage.py migrate # run the migrations

Running & Testing the project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To run the project:

.. code:: bash

    (env)$ ./manage.py runserver # the information below will be displayed if everything is okay
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    August 15, 2021 - 00:19:32
    Django version 3.2.6, using settings 'todo.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

