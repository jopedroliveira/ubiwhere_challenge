# Montrafic
Ubiwhere backend developer challenge

👨‍💻 J. Pedro Oliveira ([j.pedrodiasoliveira@gmail.com](mailto:j.pedrodiasoliveira@gmail.com))

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


