<!-- 
```bash
git clone https://github.com/Muhammadaziz-beckend/start-project.git .
```
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations account
nano .env
```
```
SECRET_KEY=bjf/sb-s=gbubguu448uuid4kngv05573
``` -->

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