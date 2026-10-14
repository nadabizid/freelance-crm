from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class AuthTests(APITestCase):
    def test_register_then_login_returns_tokens(self):
        self.client.post('/api/auth/register/', {
            'username': 'nada', 'email': 'nada@test.com',
            'password': 'secret123', 'password2': 'secret123',
        }, format='json')
        response = self.client.post('/api/auth/login/', {
            'username': 'nada', 'password': 'secret123',
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class ClientApiTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice', password='secret123')
        self.bob = User.objects.create_user('bob', password='secret123')

    def test_clients_require_authentication(self):
        response = self.client.get('/api/clients/')
        self.assertEqual(response.status_code, 401)

    def test_create_client_is_linked_to_logged_user(self):
        self.client.force_authenticate(self.alice)
        response = self.client.post('/api/clients/', {'name': 'Acme'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.alice.clients.count(), 1)

    def test_user_cannot_see_another_users_clients(self):
        self.client.force_authenticate(self.alice)
        created = self.client.post('/api/clients/', {'name': 'Acme'}, format='json')
        client_id = created.data['id']

        self.client.force_authenticate(self.bob)
        listing = self.client.get('/api/clients/')
        detail = self.client.get(f'/api/clients/{client_id}/')

        self.assertEqual(len(listing.data), 0)
        self.assertEqual(detail.status_code, 404)