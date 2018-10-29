from ecojunk.users.models import User
from django.urls import reverse
from ecojunk.users.tests.factories import UserFactory
from rest_framework import status
from ecojunk.users.api.v1.views import UserRetrieveUpdateAPIView
from test_plus import TestCase
import json
from ecojunk.users.api.v1.renderers import UserJSONRenderer
from django.test.client import Client
from rest_framework.test import APIClient
class UserAuthenticationTest(TestCase):

    def setUp(self):
        self.user = UserFactory()
        # self.client = APIClient()

    def test_api_jwt(self):
        # Create the user:
        url = '/api/v1/users'
        u = User.objects.create_user(email='user@foo.com', password='password')
        u.is_active = False
        u.save()

        ############
        # REGISTER #
        ############

        # Test register user with same username
        json_data = json.dumps({"user": {"email": "user@foo.com", "password": "password"}})
        resp = self.client.post(url + '/register', json_data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('error' in resp.data)


        # Test register user with new username
        json_data = json.dumps({"user": {"email": "user2@foo.com", "password": "password"}})
        resp = self.client.post(url + '/register', json_data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue('email' in resp.data)
        self.assertTrue('token' in resp.data)


        # Test register user with weak password
        json_data = json.dumps({"user": {"email": "user3@foo.com", "password": "pass"}})
        resp = self.client.post(url + '/register', json_data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('errors' in resp.data)
        self.assertTrue('password' in resp.data["errors"])

        #########
        # LOGIN #
        #########

        # Test login with wrong password
        json_data = json.dumps({"user": {"email": "user@foo.com", "password": "wrongone"}})
        resp = self.client.post(url + '/login', json_data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('errors' in resp.data)
        self.assertTrue('error' in resp.data["errors"])

        # Test login with wrong email
        json_data = json.dumps({"user": {"email": "wrongemail@foo.com", "password": "password"}})
        resp = self.client.post(url + '/login', json_data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('errors' in resp.data)
        self.assertTrue('error' in resp.data["errors"])

        # Test login with correct credentials
        json_data = json.dumps({"user": {"email": "user2@foo.com", "password": "password"}})
        resp = self.client.post(url + '/login', json_data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


        ##################
        # LOGGED IN USER #
        ##################

        # Test getting token
        json_data = json.dumps({"user": {"email": "user2@foo.com", "password": "password"}})
        resp = self.client.post(url + '/login', json_data, content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']

        #################
        #  MANY ERRORS  #
        #################

        # # Test getting correct token verified
        # json_data = json.dumps({"token": token})
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        # resp = client.post("/api/token-verify/", json_data, content_type='application/json')
        # print("1 token: " + str(json_data))
        # print("1 data: " + str(resp.data))
        # print("1 status: " + str(resp.status_code))
        # self.assertEqual(resp.status_code, status.HTTP_200_OK)
        #
        # # Test getting wrong token verified
        # client = APIClient()
        # json_data = json.dumps({"token": "wrongtoken"})
        # resp = client.post("/api/v1/users", json_data, content_type='application/json')
        # self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)  # bad

        # client = APIclient()
        # client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
        # resp = client.retrieve('/api/v1/users')
        # self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        # client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        # resp = client.retrieve('/api/v1/users')
        # self.assertEqual(resp.status_code, status.HTTP_200_OK)
