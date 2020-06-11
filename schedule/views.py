import os
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json
from datetime import datetime, timedelta
from .tasks import test_sample


class Home(APIView):
	def get(self, request):
		data=json.dumps(request.data)
		data=json.loads(data)
		r=test_sample.apply_async(eta=data["datetime"])
		if r:
			return Response(status=status.HTTP_200_OK)
		return Response(status=status.HTTP_404_NOT_FOUND)
