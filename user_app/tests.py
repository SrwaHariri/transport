from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='parycka', password='password123')

    def test_login(self):
        data = {
            'username': 'parycka',
            'password': 'password123'
        }
        response = self.client.post(reverse('token_obtain_pair'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
