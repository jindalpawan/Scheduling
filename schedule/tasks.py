from __future__ import absolute_import, unicode_literals
from datetime import datetime
from celery import Celery
from hero.celery import app


@app.task
def test_sample():
	print("Done")
	return 1
