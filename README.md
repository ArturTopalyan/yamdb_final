# CI и CD проекта api_yamdb

![workflow](https://github.com/lauman302/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

В проекте yamdb_final произведена настройка для приложения api_yamdb Continuous Integration и Continuous Deployment:
- автоматический запуск тестов,
- обновление образов на Docker Hub,
- автоматический деплой на боевой сервер при пуше в главную ветку master.
---
Проект реализует API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

### Технологии
Python 3.7
Django REST framework 3.12.4

### Установка проекта

#### Клонируйте данный репозиторий
```git clone https://github.com/lauman302/yamdb_final```

#### Соберите контейнеры в Docker-compose
```
docker-compose up -d
```
#### Примените миграции и соберите статику проекта

```
docker-compose exec web python manage.py migrate users
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic
docker-compose exec web python manage.py import_data  
```
#### Создайте суперпользователя
```
docker-compose exec web python manage.py createsuperuser
=======
```
#### Создайте суперпользователя
```
docker-compose exec web python manage.py import_data  
```
### Сервер и документация по API

Адрес приложения: http://localhost/api/v1/

Документация: http://localhost/redoc/