# MyApp
01_database

- setup postgres

$ psql

$ CREATE DATABASE polls;

$ \l

$ALTER DATABASE name OWNER TO new_owner;

- myapp/settings.py

DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': 'polls',
        
        'USER': 'postgres',
        
        'PASSWORD': 'postgres',
        
        'HOST': 'localhost',
        
        'PORT': '5432',
    }
}

$ python manage.py runserver

$ python manage.py migrate
