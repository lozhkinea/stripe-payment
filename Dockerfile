FROM python:3.11-slim
RUN mkdir /app
COPY ./src/requirements.txt /app
RUN pip install -r /app/requirements.txt --no-cache-dir
COPY src/ /app
WORKDIR /app
CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ]
