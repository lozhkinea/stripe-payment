# stripe-payment
Сервис, который создает платёжные формы Stripe для товаров

## Локальный запуск

Клонировать репозиторий:
```bash
git clone git@github.com:lozhkinea/stripe-payment.git
```
Создать и активировать виртуальное окружение:
```bash
cd stripe-payment
python -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python manage.py migrate
```

Создать пользователя:
```bash
python manage.py createsuperuser
```

В учетной записи Stripe получить ключи для API.
В файле src/.env задать переменные окружения (пример в .env_example).
Запустить проект:
```bash
python manage.py runserver --insecure 
```

Перtйти в браузере для заполнения базы данных:
```bash
http://localhost:8000/admin/

```

Перейти в браузере для оплаты товара 1:
```bash
http://localhost:8000/item/1/

```

Перейти в браузере для оплаты заказа 1:
```bash
http://localhost:8000/order/1/

```
## Запуск на сервере с помощью Docker:

Клонировать репозиторий:
```bash
git clone git@github.com:lozhkinea/stripe-payment.git
```

В учетной записи Stripe получить ключи для API.
В файле src/.env задать переменные окружения (пример в .env_example).
В файле src/config/settings.py указать в CSRF_TRUSTED_ORIGINS <АДРЕС_СЕРВЕРА>}.
Запустить проект:
```bash
cd stripe-payment
docker-compose up
```
Выполнить миграции:
```bash
docker-compose exec web python manage.py migrate
```

Создать пользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```


Перйти в браузере для заполнения базы данных:
```bash
http://<АДРЕС_СЕРВЕРА>}/admin/

```

Перейти в браузере для оплаты товара 1:
```bash
http://<АДРЕС_СЕРВЕРА>/item/1/

```

Перейти в браузере для оплаты заказа 1:
```bash
http://<АДРЕС_СЕРВЕРА>/order/1/
