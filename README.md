# WebBIP
Web application for Basic Image Processing (WebBIP)

## General Requirements for running with Docker

- docker
- docker-compose

### Get Start with WebBIP with docker

```bash
docker-compose up -d --build
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Running the WebBPI

```bash
docker-compose up
```
