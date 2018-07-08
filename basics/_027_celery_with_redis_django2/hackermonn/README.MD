在/hackermonn/django_with_celery这个目录下运行
> celery -A django_with_celery.celery worker -l DE
BUG -E

然后python manage.py runserver

curl 请求
> curl -x POST http://127.0.0.1:8000/api/trigger_build/

至少起了三个terminal
