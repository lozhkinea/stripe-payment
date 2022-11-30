# stripe-payment
Сервис, который создает платёжные формы Stripe для товаров

## Локальный запуск

Клонировать репозиторий:
```bash
git clone https://github.com/lozhkinea/stripe-payment.git
```

В учетной записи Stripe получить ключи для API.
В файле src/.env задать переменные окружения (пример в .env_example).

Создать и активировать виртуальное окружение:
```bash
cd stripe-payment
python -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r src/requirements.txt
```

Выполнить миграции:
```bash
python manage.py migrate
```

Создать пользователя:
```bash
python manage.py createsuperuser
```

Запустить проект:
```bash
python manage.py runserver --insecure 
```

Проект будет доступен по адресу:
```bash
http://localhost:8000/

```

## Запуск на сервере с помощью Docker:

Клонировать репозиторий:
```bash
git clone https://github.com/lozhkinea/stripe-payment.git
```

В учетной записи Stripe получить ключи для API.
В файле src/.env задать переменные окружения (пример в .env_example).
Запустить проект:
```bash
cd stripe-payment
docker-compose up
```
Выполнить миграции, собрать статику, создать пользователя:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic
docker-compose exec web python manage.py createsuperuser
```

## Проверка работы

Перейти в браузере для оплаты товара 1:
```bash
http://lea.zapto.org/item/1/

```

Перейти в браузере для оплаты заказа 1:
```bash
http://lea.zapto.org/order/1/
```

Перейти в браузере для заполнения базы данных (admin/admin):
```bash
http://lea.zapto.org/admin/

```
