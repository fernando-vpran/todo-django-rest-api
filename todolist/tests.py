from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todolist.serializers import TodolistSerializer
from todolist.models import Task

# *** Test class for basic CRUD operations on tasks ***
class TodolistTests(APITestCase):   
    def setUp(self):
        self.data = {
            "name": "Task 01"
        }
        self.response = self.client.post(
            reverse('task-list'),
            self.data,
            format="json")

    # Test creating a task
    def test_api_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, 'Task 01')

    # Test listing tasks
    def test_api_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

    # Test reading (retrieving) a task
    def test_api_read_task(self):
        task = Task.objects.get()
        response = self.client.get(
            reverse('task-detail',
            kwargs={'pk': task.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, task.name)

    # Test updating a task
    def test_api_update_task(self):
        task = Task.objects.get()
        new_data = {
            "name": "Task Updated",
            "done": True,
        }
        response = self.client.put(
            reverse('task-detail',
            kwargs={'pk': task.id}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().name, 'Task Updated')

    # Test deleting a task
    def test_api_delete_task(self):
        task = Task.objects.get()
        response = self.client.delete(
            reverse('task-detail',
            kwargs={'pk': task.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)



# *** Test class for the endpoint that filter tasks by status (done or undone) ***
class TasksByStatusTests(APITestCase):
    def setUp(self):
        self.data = {
            "name": "Task To-do",
            "done": False
        }
        self.response = self.client.post(
            reverse('task-list'),
            self.data,
            format="json")
        self.data = {
            "name": "Task Done",
            "done": True
        }
        self.response = self.client.post(
            reverse('task-list'),
            self.data,
            format="json")

    # Test retrieving tasks with 'done' status
    def test_api_get_only_done_tasks(self):
        task = Task.objects.get(done=True)
        response = self.client.get(
            reverse('tasks-by-status',
            kwargs={'status': 'done'}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.filter(done=True).count(), 1)
        self.assertContains(response, task.name)

    # Test retrieving tasks with 'undone' status
    def test_api_get_only_todo_tasks(self):
        task = Task.objects.get(done=False)
        response = self.client.get(
            reverse('tasks-by-status',
            kwargs={'status': 'undone'}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.filter(done=False).count(), 1)
        self.assertContains(response, task.name)