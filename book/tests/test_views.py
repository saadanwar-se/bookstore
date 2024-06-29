from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from django.urls import reverse
from book.models import Author, Category, Book
from book.views import AuthorViewSet, CategoryViewSet, BookViewSet
from datetime import date


class AuthorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.author = Author.objects.create(name='Test Author')

    def test_author_model(self):
        self.assertEqual(self.author.name, 'Test Author')

    def test_author_viewset_list(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('author-list'))
        force_authenticate(request, user=self.user)
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_viewset_create(self):
        factory = APIRequestFactory()
        request = factory.post(reverse('author-list'), {'name': 'New Author'})
        force_authenticate(request, user=self.user)
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_author_viewset_retrieve(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('author-detail', args=[self.author.id]))
        force_authenticate(request, user=self.user)
        view = AuthorViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.author.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_viewset_update(self):
        factory = APIRequestFactory()
        request = factory.put(reverse('author-detail', args=[self.author.id]), {'name': 'Updated Author'})
        force_authenticate(request, user=self.user)
        view = AuthorViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.author.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_viewset_delete(self):
        factory = APIRequestFactory()
        request = factory.delete(reverse('author-detail', args=[self.author.id]))
        force_authenticate(request, user=self.user)
        view = AuthorViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.author.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CategoryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')

    def test_category_model(self):
        self.assertEqual(self.category.name, 'Test Category')

    def test_category_viewset_list(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('category-list'))
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_viewset_create(self):
        factory = APIRequestFactory()
        request = factory.post(reverse('category-list'), {'name': 'New Category'})
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_viewset_retrieve(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('category-detail', args=[self.category.id]))
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.category.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_viewset_update(self):
        factory = APIRequestFactory()
        request = factory.put(reverse('category-detail', args=[self.category.id]), {'name': 'Updated Category'})
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.category.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_viewset_delete(self):
        factory = APIRequestFactory()
        request = factory.delete(reverse('category-detail', args=[self.category.id]))
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.category.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.author = Author.objects.create(name='Test Author')
        self.category = Category.objects.create(name='Test Category')
        self.book = Book.objects.create(
            title='Test Book',
            published_date=date.today(),
            isbn='1234567890123',
            category=self.category
        )
        self.book.author.add(self.author)

    def test_book_model(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.isbn, '1234567890123')
        self.assertEqual(self.book.category.name, 'Test Category')
        self.assertEqual(self.book.author.first().name, 'Test Author')

    def test_book_viewset_list(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('book-list'))
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_viewset_create(self):
        factory = APIRequestFactory()
        request = factory.post(reverse('book-list'), {
            'title': 'New Book',
            'published_date': date.today(),
            'isbn': '1234567890123',
            'category': self.category.id,
            'author': [self.author.id]
        })
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_viewset_retrieve(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('book-detail', args=[self.book.id]))
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_viewset_update(self):
        factory = APIRequestFactory()
        request = factory.put(reverse('book-detail', args=[self.book.id]), {
            'title': 'Updated Book',
            'published_date': date.today(),
            'isbn': '1234567890123',
            'category': self.category.id,
            'author': [self.author.id]
        })
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'put': 'update'})
        response = view(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_viewset_delete(self):
        factory = APIRequestFactory()
        request = factory.delete(reverse('book-detail', args=[self.book.id]))
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)