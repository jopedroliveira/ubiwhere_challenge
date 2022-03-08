# Montrafic

Ubiwhere backend developer challenge

👨‍💻 J. Pedro
Oliveira ([j.pedrodiasoliveira@gmail.com](mailto:j.pedrodiasoliveira@gmail.com))

[Postman documentation](https://documenter.getpostman.com/view/19883671/UVsEV8w9)

----

#### TL;DR

### 1. Start Server

```
$ docker-compose up
```

### 2. Load data and create a super-user

```
$ docker exec -it ubiwhere_challenge_web_1 /bin/bash
```

#### Inside the container

- Activate virtual environment

```
$ source venv/bin/activate
```

- Create a superuser

```
$ python manage.py createsuperuser --settings=ubiwhere_challenge.settings.production
```

- Load data from CSV

```
$ python manage.py load_csv trafic_speed.csv --settings=ubiwhere_challenge.settings.production
```

### 3. Run Tests (_wip_)

`docker-compose -f docker-compose.test.yml up`

----

## Project description
This project implements an API using  Django Rest Framework that allows 
users to retrieve, update and create traffic data from a geographic database.
Additionally, it allows users to sign up and sign in using the JWT approach.
When a user signup, it will be granted **_Guest_** permissions, which means it will be
able to perform GET operations.
In order to be able to perform **PUT/POST/DELETE** operations, the user must belong
to the **_Admin_** group. The promotion is performed by a superuser through 
[django admin panel](http://localhost/admin). 


## Running the project in development mode

#### Django environment
1. Install Python3.7
2. Install [Python Pip](https://pip.pypa.io/en/stable/installation/)
3. Create a virtualenvironemnt
```
$ python3 -m venv venv
```
3. Activate environment 
```
$ source venv/bin/activate
```
4. Install project requirements
```
$ pip install -m requirements.txt
```
5. Start database (dockerized)
```
$ docker-compose -f docker-compose.dev.yml
```
6. Run database migrations
```
$ python manage.py migrate --settings=ubiwhere_challenge.settings.local
```
6. Load seed data
```
$ python manage.py load_csv trafic_speed.csv --settings=ubiwhere_challenge.settings.local
```
7. Run the server
```
$ python manage.py runserver --settings=ubiwhere_challenge.settings.local
```

---

### Project notes
_This notes does not follow a specific order and may not be related to each other_

1. Intensity and characterization data is not present on database: I decided to 
not perform classification when a new velocity data is inserted, this way 
parameters can be changed without need to re-classify the data. 
Ex: The last speed entry for a given segment is 23km. For some reason, the 
classification parameter for high traffic changed from 20km to 25 km after the
entry is saved. Classifying on the fly allows to ensure all data follows the
current system, no mather when it was inserted nor the parameters changed.


2. Segment `POST` doesn't allow to directly insert speed data. This could be an
improvemnt, meaning when the user creates a new segment, speed data could
be loaded to the `body` and automatically create a speed entry.


3. Unit tests were not implemented: time limitation (personal). However, there's
a `docker-compose` file ready to run it inside a container.


4. Project is dockerized but not with production environment. Running a project
with a development server and without a reverse-proxy is not suitable for
production. Althouthg it's dockerized, an improvement would be to run the docker
with an `nginx webserver` pointing to an `WSGI` like `gunicorn`  


5. Project API documentation was [published via Postman](https://documenter.getpostman.com/view/19883671/UVsEV8w9).
