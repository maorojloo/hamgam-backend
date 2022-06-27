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
### 3here you can check the images of [admin](http://127.0.0.1:8000/admin/) panel 
![ADMIN PANEL](https://github.com/khoramism/hamgam-backend/blob/main/hamgam/jpgs/admin-panel.jpg)
<br> 
### And this is a pic of [account](http://127.0.0.1:8000/accounts/) endpoints 
![Account Endpoints](https://github.com/khoramism/hamgam-backend/blob/main/hamgam/jpgs/account-endpoints.jpg)
<br><br><br><br>
### And this is a pic of a [skill](http://127.0.0.1:8000/skill/) endpoint 
![Skill Endpoint](https://github.com/khoramism/hamgam-backend/blob/main/hamgam/jpgs/skill-endpoint.png)
<br><br><br><br>
### And this is a pic of [Idea](http://127.0.0.1:8000/ideas/) endpoint
![Idea Endpoint](https://github.com/khoramism/hamgam-backend/blob/main/hamgam/jpgs/ideas-endpoint.png)


