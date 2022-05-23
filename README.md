# Foodgram | Рецепты




- Создать файл .env в папке проекта:
```
SECRET_KEY=q^j(4)dltw(&2h@5b^4$e^(s=gm)-xm967&%kks1+n(umw!2qc
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
