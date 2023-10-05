<div align="center">

# Social Network
</div>
<br>
<hr>

## Table of Contents

- [Application functional](#functional)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Accessing the Application](#accessing-the-application)
- [Shutdown](#shutdown)
- [Demo](#demo)


<hr>

## Functional


1. CRUD for Post model;
2. Get User activity with time information about last login and last request;
3. Ability to like or unlike Posts;
4. Get analytics about how many likes was made aggregating by day;

<hr>

## Technologies

- [Django Rest Framework](https://www.django-rest-framework.org)
<br>Django Rest Framework is a powerful and flexible toolkit for building Web APIs.


- [Postgres](https://www.postgresql.org/docs/)
<br>Postgres is a powerful, open-source object-relational database system. 
<br>In this project, it is used as the main data store, exposed on port 5432.
<hr>



## Prerequisites

1. Make sure you have Docker and Docker Compose installed on your system. 
You can check the installation instructions [here for Docker](https://docs.docker.com/get-docker/) 
and [here for Docker Compose](https://docs.docker.com/compose/install/).

<hr>

## Setup

1. Clone the project:
```
git clone https://github.com/volodymyr-komarnyckyi/social_network
```
2. Navigate to the project directory:
```
cd social_network
```
3. Сreate your `.env` file taking as an example `.env.example` file.


4. Build and run the Docker containers:
```
docker-compose build
docker-compose up
```

<hr>

## Accessing the Application

### Documentation is accessible at:
1. `http://localhost:8000/api/v1/doc/swagger/`
2. `http://localhost:8000/api/v1/doc/redoc/`

## Endpoints
   ```
   "post" : 
                "http://127.0.0.1:8000/api/posts/"
                "http://127.0.0.1:8000/api/posts/<int:pk>/"
                "http://127.0.0.1:8000/api/posts/<int:pk>/like/"
                "http://127.0.0.1:8000/api/posts/<int:pk>/unlike/"
                "http://127.0.0.1:8000/api/analitics/?date_from=YY-MM-DD&date_to=YY-MM-DD"
   "user" : 
                "http://127.0.0.1:8000/api/user/register/"
                "http://127.0.0.1:8000/api/user/me/"
                "http://127.0.0.1:8000/api/user/token/"
                "http://127.0.0.1:8000/api/user/token/refresh/"
                "http://127.0.0.1:8000/api/user/token/verify/"
                "http://127.0.0.1:8000/api/user/activity/"
   ```

<hr>

## Shutdown

1. To stop running the server use CTRL-C

<hr>

## Demo

![Website Interface](readme_images/post_list.jpg)
![Website Interface](readme_images/post_detail.jpg)
![Website Interface](readme_images/post_like.jpg)
![Website Interface](readme_images/post_unlike.jpg)
![Website Interface](readme_images/post_unlike.jpg)
![Website Interface](readme_images/analytics.jpg)
![Website Interface](readme_images/user_activity.jpg)

<hr>

Remember to replace `localhost` with the relevant 
IP address if you're not accessing these 
from the same machine where the services are running.

<hr>