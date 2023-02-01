# HospitacjePODjango
 
## Setup venv and install requirements:

(Windows)
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements
```

## Apply migrations
```
python manage.py migrate
```
## (only on deploy) collect static files
```
python manage.py collectstatic
```

## Run application
```
python manage.py runserver
```
