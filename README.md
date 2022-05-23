# Foodgram | Рецепты
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
![Django-app workflow](https://github.com/aleksej-redin/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

### Доступ в админ панель
```
- Username: root
- Password: rootfoodgram
```

## Запуск проекта
- Клонировать репозиторий GitHub:
```
https://github.com/aleksej-redin/foodgram-project-react.git
```

- Создать файл .env в папке проекта:
```
SECRET_KEY=django-insecure-q^j(4)dltw(&2h@5b^4$e^(s=gm)-xm967&%kks1+n(umw!2qc
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DEBUG=True
```

- в Docker cобрать  контейнеры:
```
docker-compose up -d
```
- Список контейнеров, можно посмотреть при помощи команды:  
```
docker-compose ps -a
```  
- Выполнить миграции, создать суперпользователя, собрать статику:
```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input 
```
- Импорт данных из файла ingredients.json:
```
docker-compose exec backend python manage.py shell
>>> exec(open("./data/import_json.py").read())
>>> exit()
```

### Веб-адреса проекта:
```
http://51.250.26.246/ - главная страница
http://51.250.26.246/admin/ - панель администратора
http://51.250.26.246/api/docs/ - документация API