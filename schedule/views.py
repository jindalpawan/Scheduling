import os
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ImproperlyConfigured
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.utils import timezone
from datetime import datetime, timedelta
from .tasks import hello, temp

'''
class Home(TemplateView):
	def get(self, request):
		print((datetime.now()+timedelta(minutes=1)))
		hello.apply_async(eta=(datetime.now()+timedelta(minutes=1)))
		return HttpResponse()
'''

class Home(APIView):
	def get(self, request):
		data=json.dumps(request.data)
		data=json.loads(data)
		hello.apply_async(eta=data["datetime"])
		if temp:
			dic={'response':"Success"}
		else:
			dic={'response':"Failed"}
		return Response(dic)
