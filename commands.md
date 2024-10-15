docker compose up

celery -A dcs worker --beat -l info

django-admin startproject dcs .

python manage.py shell

python manage.py runserver

python manage.py makemigrations

python manage.py migrate

python manage.py startapp movies
