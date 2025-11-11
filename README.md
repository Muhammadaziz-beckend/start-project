# Быстрый запуск проекта
```
bash <(curl -s https://raw.githubusercontent.com/Muhammadaziz-beckend/start-project/main/start.sh)
```

# Start Project Backend Template

Это шаблон backend-проекта на Django и Django REST Framework. Подходит для быстрых стартов API.

## Основные возможности

- Django 5.x
- Django REST Framework
- DRF Spectacular для автогенерации OpenAPI/Swagger документации
<!-- - JWT авторизация (SimpleJWT) -->
- Разделение настроек на dev/prod
- Подготовленная структура для масштабируемых модулей
- Готовый CORS и middleware
- Подключена обработка ошибок и логирование

---

## Используемые технологии

- Python 3.12
- Django
- Django REST Framework
- DRF Spectacular (Swagger/OpenAPI)
- PostgreSQL / SQLite
- Docker (опционально)

---

## Структура проекта

```

├── api
│   ├── docs.py
│   ├── urls.py
│   ├── __init__.py
│   └── v1
│       └── urls.py
│       ├── __init__.py
├── apps
│   ├── account
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── manager.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── __init__.py
├── core
│   ├── __init__.py
│   ├── asgi.py
│   ├── config_drf.py
│   ├── config.py
│   ├── constants.py
│   ├── cors.py
│   ├── database.py
│   ├── media.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── media
│   └── qwe
├── README.md
├── requirements.txt
├── static
│   └── static_dirs
└── utils
    ├── data_base.py
    ├── __init__.py
    ├── mixins.py
    ├── models.py
    ├── paginations.py
    └── permissions.py
```

# 🚀 Запуск проекта

## 1) Создания папки

```
mkdir <name dir>
cd <name dir>
```

## 2) клонирования из репозитории

``` bash
git clone https://github.com/Muhammadaziz-beckend/start-project.git .
```

## 3) Создания venv скачиваем зависимости из requirements.txt и делаем миграцию

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations account
python manage.py makemigrations
python manage.py migrate
```

## 3) Создаём .env фйл 

```
nano .env
```

### └─ В .env записываем 

```
PORT_WEB=8000
SECRET_KEY=bjf/kot/sb-s=gbubguu448uuid4kngv05572

# Database
POSTGRES_DB=db
POSTGRES_USER=admin
POSTGRES_PASSWORD=supper_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

## 4) Запуск проекта

```
python mange.py runserver 8000
```