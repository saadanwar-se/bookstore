from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from django.urls import reverse
from book.models import Author
from book.views import AuthorViewSet


class AuthorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.author = Author.objects.create(name='Test Author', biography='Test Biography')

    def test_author_model(self):
        self.assertEqual(self.author.name, 'Test Author')