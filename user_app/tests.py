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
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    # def test_logout(self):
    #     self.token = Token.objects.get(user__username='parycka')
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    #     message = 'lerama'
    #     print(message,self.token.key)
    #    #  response = self.client.post(reverse('logout'))
    #    #  self.assertEqual(response.status_code, status.HTTP_200_OK)