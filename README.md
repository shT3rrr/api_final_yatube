# Yatube API

Бэкенд API для социальной платформы Yatube. Позволяет управлять постами, комментариями, группами и подписками. Аутентификация через JWT.

## Установка

1.  Клонировать репозиторий:
    `git clone <URL_репозитория>`
    `cd api_final_yatube`
2.  Создать и активировать venv:
    `python -m venv venv`
    `source venv/bin/activate` (Linux/macOS) или `venv\Scripts\activate` (Windows)
3.  Установить зависимости:
    `pip install -r requirements.txt`
4.  Миграции (в директории `yatube_api`):
    `python manage.py migrate`
5.  Запуск сервера:
    `python manage.py runserver`

API будет доступно на `http://127.0.0.1:8000/api/v1/`.
Документация ReDoc: `http://127.0.0.1:8000/redoc/`.
