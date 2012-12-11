from celery import task
from arduino import refresh_loop

@task()
def add(x, y):
    return x + y
    
@task()
def ardperiotic():
	l = refresh_loop()
	l.loop()
	
