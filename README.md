# Тестовое "Examus"
## Автор
- [AlexeyPlz](https://github.com/AlexeyPlz)
## Проверка проекта
[![Flake8](https://github.com/AlexeyPlz/Test_Examus/actions/workflows/codestyle.yml/badge.svg)](https://github.com/AlexeyPlz/Test_Examus/actions/workflows/codestyle.yml)
## Стек
- Python 3.10
- JavaScript
- Pipenv 2023.6.26
- Django 3.2.19
- DRF 3.14.0
- DRF Extra-Fields 3.5.0
- Dotenv 1.0.0
- Pillow 9.5.0
- Gunicorn 20.1.0
- Psycopg2 Binary 2.9.6
## Задание
Написать на Django и DRF приложение "Меню ресторана".  
У каждого пункта меню есть:
- Категория;
- Название;
- Энергетическая ценность;
- Цена;
- Изображение;
- Список аллергенов.

В приложении две страницы:
- Меню - выводится список всех блюд, сгруппированных по категориям. Любое блюдо можно добавить в заказ несколько раз;
- Заказы - выводится список заказанных на предыдущей странице блюд и их аллергенов, сумма заказа.

У приложения есть API с двумя эндпоинтами:
- Получение списка всех блюд;
- Добавление нового блюда.

В качестве защиты API используется один токен, указываемый в настройках приложения.  
Настроить локальную разработку на основе Docker и Docker-Compose, использовать базу данных PostgreSQL.  

Опционально:
- Использовать библиотеку для управления зависимостями pipenv.
- Написать тест на API метод добавления блюда в меню.
## Особенности и логика работы
Для работы проекта необходимы куки, так как в них записываются следующие данные:
- device - Уникальный UUID девайса пользователя для его идентификации;
- order - Массив данных для хранения выбранных блюд в меню.

На главной странице можно выбрать подходящие блюда, нажимая на "+" и "-" можно изменять количество порций.  
Максимум можно добавить 10 порций одного блюда.  
После этого необходимо перейти в раздел заказы.  
В данном разделе будет указан список всех прошлых заказов и то, что вы выбрали в меню на прошлой странице.  
После нажатия на кнопку "Создать заказ" все выбранные блюда будут добавлены в новый заказ.

Для доступа к API необходимо прописать токен в параметр "API-Token-Access" в Headers.
## Интерфейс
- ToDo
## Запуск локально в контейнере
Запустите контейнеры в фоновом режиме:
```bash
sudo docker-compose up -d
```
Проведите миграции:
```bash
sudo docker-compose exec app python manage.py makemigrations
sudo docker-compose exec app python manage.py migrate
```
Соберите статику:
```bash
sudo docker-compose exec app python manage.py collectstatic --no-input 
```
Создайте суперпользователя:
```bash
sudo docker-compose exec app python manage.py createsuperuser
```
Если необходимы манипуляции с Docker:
```bash
sudo docker-compose up --build -d      # Пересобрать контейнеры
sudo docker-compose down               # Удаление контейнеров
sudo docker-compose down  --volumes    # Удаление контейнеров с томами
```
## Доступ после запуска
- http://localhost/
- http://localhost/admin/
## Роутеры API
В проекте доступен один роутер:
- http://localhost/api/v1/dishes/ [GET, POST]

Схема POST запроса:
```python
{
    "title": str,
    "price": int,
    "calories": int,
    "image": base64,
    "category": int,
    "allergens": list[int]
}
```
Параметры GET запроса:
- limit - количество блюд на страницу
- page - номер страницы

Схема GET запроса:
```python
{
    "count": int,
    "next": str | None,
    "previous": str | None,
    "results": [
        {
            "id": int,
            "title": str,
            "price": int,
            "calories": int,
            "image": str,
            "category": {
                "id": int,
                "created": datetime,
                "updated": datetime,
                "title": str
            },
            "allergens": [
                {
                    "id": int,
                    "created": datetime,
                    "updated": datetime,
                    "title": str
                }
            ],
            "created": datetime,
            "updated": datetime
        }
    ]
}
```