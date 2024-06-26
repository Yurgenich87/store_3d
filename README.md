# Краткое описание дипломной работы

Дипломная работа представляет собой веб-приложение для интернет-магазина по продаже 3D-моделей и 3D-принтов. Приложение реализовано с использованием фреймворка Django и Django REST framework для обеспечения бэкэнда, а также jQuery и Bootstrap для фронтенда.
![Главная страница](index.png)
## Основные функциональности:

- Регистрация и аутентификация пользователей.
- Управление товарами, включая создание, редактирование и удаление.
- Заказы и корзина покупок для зарегистрированных пользователей.
- Фильтрация товаров по различным критериям.
- Административная панель для управления товарами и заказами.
- API для доступа к данным о пользователях, товарам и заказах.

## Дополнительные особенности:

- Использование механизмов кэширования для повышения производительности и уменьшения нагрузки на сервер базы данных.
- Обработка асинхронных задач с использованием Celery и Redis в качестве брокера сообщений.
- Хранение данных о заказах и пользователях в реляционной базе данных (MySQL или PostgreSQL).
- Хранение статических файлов, таких как изображения товаров, в облачном хранилище с использованием django-storages.

## Дополнительная информация:

Код проекта содержит подробные комментарии и инструкции по настройке, развертыванию и использованию.
