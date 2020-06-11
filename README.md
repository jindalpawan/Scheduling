Scheduling
=============

# Installation

This project is running on Ubuntu, so this is
probably the easiest environment in which to get things running, but other
distributions of linux should be fine as well.

### Virtual environment (if your system doesn't have it already):

The development environment relies on using a Python [virtual environment][venv]
for tools and portability across platforms. Ensure that you have Python Pip
installed for your platform before proceeding with these instructions.

Windows users can use the [following guide][windows venv]. Specifically, get
Python installed and then use the get-pip.py installer once Python is working

OSX users can use the built in version of Python as long as Pip is available,
or better, install [Brew and Python][osx venv].

Linux users should have Python already installed. Ensure Pip is installed via
your package manager and you should be all set.


## Linux based Setup for development

Note: Ubuntu 16.04 LTS is recommended to use for the development environment.

1. Run the following git clone (specify a directory of your choosing if you like):

        git clone https://github.com/jindalpawan/Scheduling


2. cd into the name of the directory into which you cloned the git repository

        cd hero

3. After activating the virtual environment, install the dependencies

        pip install -r requirements.txt

4. You are all set. Run the migrate command

        python manage.py migrate

        
5. You are all set. Run the final command

        python manage.py runserver

6. You are all set. Run the celery final command

        celery -A hero worker --loglevel=info

7. Its time to rock. Visit [http://localhost:8000][localhost] in your browser and you should be all set.


[venv]: http://pypi.python.org/pypi/virtualenv
[wrapper]: http://www.doughellmann.com/projects/virtualenvwrapper/
[windows venv]: http://docs.python-guide.org/en/latest/starting/install/win/
[osx venv]: http://docs.python-guide.org/en/latest/starting/install/osx/
[localhost]: http://localhost:8000/