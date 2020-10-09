# Event Management System

### Codename: Evite
Evite is an event management system for subscribe/signup for an event also can unsubscribe from the event.
For signup/subscribe user need an email address.

### Prerequisites
Make sure you have installed Python 3, Git and virtual environment on your device

### Project structure
```
* Evite/
  |--- event/
  |    |--- migrations/
  |    |--- templates/
  |    |--- __init__.py
  |    |--- admin.py
  |    |--- apps.py
  |    |--- forms.py
  |    |--- models.py
  |    |--- tests.py
  |    |--- urls.py
  |    |--- views.py
  |--- Evite/
  |    |--- __init__.py
  |    |--- settings.py
  |    |--- urls.py
  |    |--- wsgi.py
  |--- eviteapi/
  |    |--- migrations/
  |    |--- __init__.py
  |    |--- admin.py
  |    |--- apps.py
  |    |--- models.py
  |    |--- serializers.py
  |    |--- tests.py
  |    |--- urls.py
  |    |--- views.py
  |--- .gitignore
  |--- db.sqlite3
  |--- LICENSE
  |--- manage.py
  |--- README.md
  |--- requirements.txt
  
```


### Clone and RUN 
Now run it for clone the project:  
$ cd "your-workspace"  
$ git clone  https://github.com/rasselict07/Evite

Enter the project and take a look around:  
$ cd Evite/  
$ ls  
$ pip install -r requirements.txt  
$ python manage.py migrate --run-syncdb  
$ python manage.py migrate  
$ python manage.py runserver

Will find a url in terminal:  
"Starting development server at http://127.0.0.1:8000/"  
Browse application through that url   

For admin we have admin panel like http://127.0.0.1:8000/admin/  
Default User: admin  
Default Password: 123456  
Admin can create new user, Group, Events, API token for user and Event User mapping.

For check the API execute this command in terminal  
```curl -X GET http://127.0.0.1:8000/api/events/events/ -H "Authorization: Token 7248ce0a5682f425cbb22297e427f0d4e5626de5"```  
For access api need authorization token. you can add token through admin panel for user, like for admin "7248ce0a5682f425cbb22297e427f0d4e5626de5"  this token is available

Thanks!!