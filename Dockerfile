FROM python:3.6
LABEL maintainer="LucyKFletcher@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

RUN apt update && \
    apt install -y nginx && \
    rm -v /etc/nginx/nginx.conf && \
    rm -v /etc/nginx/sites-enabled/default && \
    chown -R www-data:www-data /var/lib/nginx /var/log/nginx && \
    chmod -R 777 /var/lib/nginx /var/log/nginx

COPY ./nginx.conf /etc/nginx/

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt && \
    pip install gunicorn

COPY ./photography /code/
WORKDIR /code

RUN mkdir /code/logs && \
    touch /code/logs/access.log /code/logs/error.log && \
    python manage.py collectstatic && \
    python manage.py migrate && \
    useradd wagtail && \
    chown -R wagtail /code

EXPOSE 80
CMD /etc/init.d/nginx start && gunicorn --access-logfile - --workers 3 --bind 127.0.0.1:8000 --chdir /code/photography photography.wsgi:application