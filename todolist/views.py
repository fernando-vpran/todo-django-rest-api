from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from todolist.models import Task
from todolist.serializers import TodolistSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def task_list(request):
    # GET list of tasks
    if request.method == 'GET':
        tasks = Task.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            tasks = tasks.filter(name__icontains=name)
        
        tasks_serializer = TodolistSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    
    # POST a new task
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TodolistSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE all tasks
    elif request.method == 'DELETE':
        count = Task.objects.all().delete()
        return JsonResponse({'message': '{} Tasks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    # find task by pk (id)
    try: 
        task = Task.objects.get(pk=pk) 
    except Task.DoesNotExist: 
        return JsonResponse({'message': 'The task does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET task
    if request.method == 'GET': 
        task_serializer = TodolistSerializer(task) 
        return JsonResponse(task_serializer.data) 
    
    # PUT (update) task
    elif request.method == 'PUT': 
        task_data = JSONParser().parse(request) 
        task_serializer = TodolistSerializer(task, data=task_data) 
        if task_serializer.is_valid(): 
            task_serializer.save() 
            return JsonResponse(task_serializer.data) 
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    # DELETE task
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def tasks_by_status(request, status):
    # GET tasks by status (done or not done)
    if status == 'done':
        tasks = Task.objects.filter(done=True)
    elif status == 'undone':
        tasks = Task.objects.filter(done=False)
    else:
        return JsonResponse({'message': 'Invalid status parameter'}, status=status.HTTP_400_BAD_REQUEST)

    tasks_serializer = TodolistSerializer(tasks, many=True)
    return JsonResponse(tasks_serializer.data, safe=False)