# Building an E-learningplatform

## Commands
- pip install pipenv
- pipenv install django
- django-admin startproject kidco .
- python manage.py startapp courses
- python manage.py migrate
- python manage.py runserver
- code .
- pipenv --venv
- **virtualenvpath\bin\python**
- python --version
- python -m django --version
- pipenv install python-dotenv
- pipenv install Pillow==9.2.0
- pipenv install mysqlclient
- mysql --version 
- mysql -u root -p
- python manage.py createsuperuser
- python manage.py dumpdata courses --indent=2
- mkdir courses/fixtures
- python manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
- python manage.py shell

### Steps
- Activate virtual environment by running pipenv --venv --> command pallette --> select interpreter
- Make migrations

#### Notes
- Created a *fixtures*
- Created a default ordering for *course* and *modules*
- Used model inheritance to manage different types of content for the course modules
- Implemented a custom model field
- Created an authenetication system for the E-learning platform