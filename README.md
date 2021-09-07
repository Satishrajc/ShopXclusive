# ShopXclusive

This is the brand-new website to buy/sell the home needs.

### Basic Django project setup:

#### Create et access project folder
mkdir <project_name> 

cd <project_name> 

#### Create Python virtual env 
python3 -m venv <environment name>

#### Activate virtual env
source <environment name>/bin/activate

#### If you want to deactivate virtual env
deactivate

#### Install django
pip install django

#### New django project 
django-admin startproject <project_name>

#### Run the django and check for installation
python manage.py runserver —> Run Server (http://127.0.0.1:8000) CTRL+C to stop

#### Create app 
python manage.py startapp <app_name>

#### Migrate the changes to database
1. Python manage.py migrate
2. Python manage.py makemigrations <app_name>
3. Python manage.py migrate