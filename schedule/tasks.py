from __future__ import absolute_import, unicode_literals
from datetime import datetime, timedelta
from celery import Celery
from celery import shared_task,current_task, task
from hero.celery import app


temp=0

@app.task
def hello():
	temp=1
	return 1
