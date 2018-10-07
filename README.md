# django_test2

Countries & Cities Sorting app.


#Building
$python3 -m venv testing
$source testing/Scripts/activate
$python3 -m pip install --upgrade pip
$pip install -r requirements.txt
$python manage.py makemigrations
$python manage.py migrate
$winpty python manage.py createsuperuser
$python manage.py runserver


Then visit http://localhost:8000 to view the app. 

# requirements

See REQUIREMENTS in the requirements.txt file for additional dependencies

