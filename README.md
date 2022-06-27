# hamgam-backend
This is the Backend for the HamGam Project 

this is how you start the project 
first make a virtualenv 
 ```bash 
 virtualenv env
 ```
 and then we activate it and move to this folder 
 ```bash
 source env/bin/activate
 cd hamgam
 ``` 
 then we install the required packages 
 ```bash 
 pip install -r Requirements/dev.txt
 ```
 and then we are already to go and makemigrations and run the server 
 so first we change dir 
 ```bash 
 cd hamgam-backend
 ```
 and then we make the migrations and migrate them to the db 
 ```bash 
 python manage.py makemigrations
 python manage.py migrate
```
and then let's run the server 
```bash 
python manage.py runserver
```
now let's head to the 127.0.0.1:8000 port to see the api


