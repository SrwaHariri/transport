from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from transportation_app.api import serializers
from transportation_app import models


class TransportationTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.item = models.TransportItem.objects.create(name="mazda",
                                                           transport_model="versionone")

    def test_TransportItem_create(self):
        data = {
            'name': 'kia',
            'transport_model': 'celtos',
            'colors': 'white',
            'category': 'car'
        }
        response = self.client.post(reverse('item-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_TransportItem_list(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_TranscformItem_ind(self):
        response = self.client.get(reverse('item-detail', args=(self.item.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_TransportItem_update(self):
        data = {
            'name': 'kia',
            'transport_model': 'celtos',
            'colors': 'white',
            'category': 1
        }
        response = self.client.put(reverse('item-detail', args=(self.item.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

