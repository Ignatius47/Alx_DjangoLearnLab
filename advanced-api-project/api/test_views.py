from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})

        # Create a user and token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_authentication_required(self):
        self.client.credentials()  # Remove authentication
        url = reverse('book-list')
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2022,
            'author': self.author.id
        }
         response = self.client.post(url, data, format='json')
         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')
    def test_authentication_required(self):
        self.client.logout()  # Log out the user
        url = reverse('book-list')
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)





    
