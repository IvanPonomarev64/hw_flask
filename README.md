# Домашнее задание к лекции «Celery»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория.

## Задание* (необязательное)

Для написанного раннее сервиса, например [этого](../2.1-flask), необходимо реализовать метод API, рассылающий email всем пользователям. Поскольку 
пользователей может быть очень много, метод должен работать асинхронно: 
- POST запрос создает задачу на рассылку, отправляет в Celery и возвращает task_id ,
- GET с параметром task_id в uri возвращает статус задачи.

Дополнительно: добавьте фильтры, чтобы сообщения отправлялись не всем пользователям, а только соответствующим определенным параметрам, передаваемым в POST запросе.


Результатом работы является API с методом массовой рассылки.

### Шаги для выполнения:
1. Первым запускаем файл '''settings.py''' в нем создается приложение, bcrypt, сессия и соединение с бд

2. В файле '''app.py''' создаются все необходимые таблицы и запускается приложение

3. В файле '''client.py''' находятся все требуемые запросы
