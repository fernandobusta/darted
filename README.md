# darted
Commercial Website for Darted - in Django


## In the Procfile
The web: prefix tells Railway that this is a web process and can be sent HTTP traffic. We then call the command Django migration command python manage.py migrate to set up the database tables. Next, we call the Django command python manage.py collectstatic to collect static files into the folder defined by the STATIC_ROOT project setting (see the section serving static files in production below). Finally, we start the gunicorn process, a popular web application server, passing it configuration information in the module locallibrary.wsgi (created with our application skeleton: /locallibrary/wsgi.py).


## For static files
- STATIC_URL: This is the base URL location from which static files will be served, for example on a CDN.
- STATIC_ROOT: This is the absolute path to a directory where Django's collectstatic tool will gather any static files referenced in our templates. Once collected, these can then be uploaded as a group to wherever the files are to be hosted.
- STATICFILES_DIRS: This lists additional directories that Django's collectstatic tool should search for static files.


# SETTINGS
## Deployment
Settings folder defines configuration for production and development.
Secret key should be an environment variable in server

### MIDDLEWARE
Middleware will be handled separatly for production environment
