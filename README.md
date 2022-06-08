# Personal management system


# Getting Started

```sh
$ git clone https://github.com/jsan-95/personal_management_system.git
$ cd personal_management_system
$ sudo docker-compose run web
Open another terminal
$ docker exec -t -i $(sudo docker ps -aqf "name=personalmanagementsystem_web") bash
$ python manage.py createsuperuser
Close terminal 
Back to terminal with docker
$ CONTROL-C 
$ sudo docker-compose up
```
Application is started at 
```sh
0.0.0.0:8000
```

URLS
----

/login: page of login. Before login you have to create user in /admin
/ or /profile: page of profile data. Here you can modify avatar, the rest of fields and logout 

***

