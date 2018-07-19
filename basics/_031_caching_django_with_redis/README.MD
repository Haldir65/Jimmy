https://code.tutsplus.com/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178

view the difference between those two backends
loadtest -n 1000 -k  http://localhost:8000/store/cache
loadtest -n 1000 -k  http://localhost:8000/store/
