#!/bin/bash
rm -rf dialinginapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations dialinginapi
python manage.py migrate dialinginapi
python manage.py loaddata methods
python manage.py loaddata users
python manage.py loaddata grinds
python manage.py loaddata recipes
python manage.py loaddata method_equipment
python manage.py loaddata recipe_equipment
python manage.py loaddata steps
python manage.py loaddata owner
