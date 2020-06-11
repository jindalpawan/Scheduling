from __future__ import absolute_import, unicode_literals
from datetime import datetime, timedelta
from celery import Celery
from celery import shared_task,current_task, task
from hero.celery import app



@app.task
def hello():
	x()
	return "abx"

def x():
	print("xchjkl")


if __name__ == '__main__':
    app.start()