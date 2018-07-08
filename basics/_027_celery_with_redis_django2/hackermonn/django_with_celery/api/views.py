from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class BuildTrigger(APIView):
  def post(self, request):
    # build_something() # This would take 1 minute to finish
    build_something.apply_async()
    return Response(None, status=201)


from celery import shared_task
@shared_task
def build_something():
  # some code here
  print('we are doing some expensive work here ===========')
