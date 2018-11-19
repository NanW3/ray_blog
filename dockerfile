FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD ./my_blog /app
ADD ./requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app
RUN apt-get update && apt-get -y install sqlite3
RUN python manage.py makemigrations && python manage.py migrate
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
