# Simple Resume Scanner

This is a Simple Resume Scanner using PyPDF2

Its a Python 3 application

## Step 1 [Install Requirements]

`pip install requirements.txt`

## Step 2 [Start Application]

`python manage.py runserver`

## Other Commands

To initialize a db

`python db init`

To make migration files

`python manage.py db migrate`

To upgrade database

`python manage.py db upgrade`

## API

GET /filter
Arguments: path : <full path of the local directory>
           q    : <query word to searched in the resumes>

__Example__ : `http://127.0.0.1:5000/filter?path=C:\Users\DELL\Desktop\Git\ResumeScanner\app\static\resume&q=sql` 
