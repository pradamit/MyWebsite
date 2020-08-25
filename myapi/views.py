from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from mysite.models import user_details

@api_view(["POST"])
def sample(request):
    try:
        height = json.loads(request.body)
        #print(height)
        #weight = str(user_details.objects.all())
        return JsonResponse("weight is : "+str(height), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)