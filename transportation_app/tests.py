from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from transportation_app.api import serializers
from transportation_app import models


class TransportItemTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.item = models.TransportItem.objects.create(name="mazda", transport_model="versionone")


    def test_TransportItem_create(self):
        data = {
            'name': 'kia',
            'transport_model': 'celtos',
            'colors': 'white',
            'category': 'car'
        }
        response = self.client.post(reverse('item-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_TransportItem_list(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_TransformItem_ind(self):
        response = self.client.get(reverse('item-detail', args=(self.item.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_TransportItem_updatelist(self):
        data = {
            'name': 'kia',
            'transport_model': 'celtos',
            'colors': 'white',
            'category': 1
        }
        response = self.client.put(reverse('item-detail', args=(self.item.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_TransportItem_updateind(self):
        data = {
            'name': 'kia',
            'transport_model': 'celtos',
            'colors': 'white',
            'category': 1
        }
        response = self.client.put(reverse('item-detail', args=(self.item.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_TransportItem_update(self):
        data = {
            'name': 'kia',
            'transport_model': 'celtos',
            'colors': 'white',
            'category': 1
        }
        response = self.client.put(reverse('item-detail', args=(self.item.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_TransportItem_delete(self):
        data = {
            'name': 'kia',
            'transport_model': 'celtos',
            'colors': 'white',
            'category': 1
        }
        response = self.client.delete(reverse('item-detail', args=(self.item.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class CategoryTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.item = models.TransportItem.objects.create(name="mazda",
                                                        transport_model="versionone")
        self.category = models.Category.objects.create(name="mazda")

    def test_category_create(self):
        data = {
            'name': 'ships',
            'parent': 'yacht'
        }
        response = self.client.post(reverse('category-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_list(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_ind(self):
        response = self.client.get(reverse('category-detail', args=(self.category.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 1)
        self.assertEqual(models.Category.objects.get().name, 'mazda')

    def test_category_update(self):
        data = {
            'name': 'kia',
            'parent': 'vehicles',
        }
        response = self.client.put(reverse('category-detail', args=(self.category.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_TransportItem_delete(self):
        data = {
            'name': 'kia',
            'parent': 'vehicles',
        }
        response = self.client.delete(reverse('item-detail', args=(self.category.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ColorTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.item = models.TransportItem.objects.create(name="mazda",
                                                        transport_model="versionone")
        self.category = models.Category.objects.create(name=self.item)
        self.color = models.Color.objects.create(name="yellow")

    def test_color_create(self):
        data = {
            'name': 'white',
        }
        response = self.client.post(reverse('color-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_color_ind(self):
        response = self.client.get(reverse('color-detail', args=(self.color.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_color_list(self):
        response = self.client.get(reverse('color-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_color_updatelist(self):
        data = {
            'name': 'white',
        }
        response = self.client.put(reverse('color-list'), data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_color_updateind(self):
        data = {
            'name': 'white',
        }
        response = self.client.put(reverse('color-detail', args=(self.color.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK )