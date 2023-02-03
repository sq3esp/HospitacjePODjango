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

##write data to fixtures
```
python -Xutf8 manage.py dumpdata hospitation_manager -o C:\HospitacjePODjango\hospitation_manager\fixtures\hospitation_manager.json
```

## Load data from fixtures
```
python manage.py loaddata hospitation_manager
```

## Run application
```
python manage.py runserver
```
