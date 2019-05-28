from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import urllib
from django.http import JsonResponse

#all the method and classes are in models section
from .models import Process, Schedular


#scheduler request handeler
@api_view(['POST']) 
def schedularHandeler(request):
  ProcessList = []

  try:
    #loading json data
    json_data = json.loads(request.body)
    json_list = json_data['list']

    #converting json list of processes into list of class objects
    for x in json_list:
      ProcessList.append(Process(x['pid'], x['bt'], x['art']))
      
    #checking the scheduler type
    if json_data['type'] == 'FCFS':
      ProcessList = Schedular.FCFS(ProcessList)
    elif json_data['type'] == 'SJF':
      ProcessList = Schedular.SJF(ProcessList)
    else:  
      return Response('Invalid Type of sheduler')

    # loading json data and returning it
    json_data = json.loads(ProcessList)
    # print(json_data)
    return Response(json_data)
  except:
    return Response('The input data is not correct')

@api_view(['GET'])
def default(request):
  return Response('<h2>default</h2>')  