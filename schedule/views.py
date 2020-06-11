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
from .tasks import hello


class Home(TemplateView):
	def get(self, request):
		print((datetime.now()+timedelta(minutes=1)))
		r=hello.apply_async(eta=(datetime.now()))
		print(r, "sdffdsawed")
		return HttpResponse("aa")

'''
class Home(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		data=json.dumps(request.data)
		data=json.loads(data)
		return Response(serializer)
'''