DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': {{ mysql_db_name }},
        'USER': {{ msyql_user }},
        'PASSWORD': {{ mysql_pwd }},
        'HOST': '{{ mysql_ip }}',
        'PORT': '3306',
    }
}
