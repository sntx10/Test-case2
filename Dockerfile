FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
COPY ./init-mongo.js /docker-entrypoint-initdb.d/
RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
