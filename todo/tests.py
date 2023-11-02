# todo/tests.py
 
import datetime
 
from django.db.models import QuerySet
from django.http import HttpResponse
from django.urls import reverse
from django.test import TestCase, Client
 
from todo.models import Task
 
class TestTaskModel(TestCase):
     ...
 
class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("index")
        cls.client = Client()
        cls.task = Task.objects.create(name="book dentist appointment")
 
    def test_index_view_returns_httpresponse(self):
        """Test our view returns a HttpResponse"""
 
        response = self.client.get(self.url)
 
        self.assertTrue(isinstance(response, HttpResponse))
 
    def test_status_code(self):
        response = self.client.get(self.url)
 
        self.assertEqual(response.status_code, 200)
 
    def test_context(self):
        """Tests the context contains queryset of tasks"""
        response = self.client.get(self.url)
 
        self.assertIn("tasks", response.context)
 
        tasks = response.context["tasks"]
 
        self.assertTrue(isinstance(tasks, QuerySet))
        self.assertEqual(tasks.first(), self.task)
 
    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "temp_index.html")