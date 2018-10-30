import json

from rest_framework import status
from test_plus import TestCase

from ecojunk.users.models import User
from ecojunk.users.tests.factories import UserFactory


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        # self.client = APIClient()

    def test_api_jwt(self):
        # Create the user:
        url = "/api/v1/users"
        u = User.objects.create_user(email="user@foo.com", password="password")
        u.is_active = False
        u.save()

        ############
        # REGISTER #
        ############

        # Test register user with same username
        json_data = json.dumps(
            {"user": {"email": "user@foo.com", "password": "password"}}
        )
        resp = self.client.post(
            url + "/register", json_data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("error" in resp.data)

        # Test register user with new username
        json_data = json.dumps(
            {"user": {"email": "user2@foo.com", "password": "password"}}
        )
        resp = self.client.post(
            url + "/register", json_data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue("email" in resp.data)
        self.assertTrue("token" in resp.data)

        # Test register user with weak password
        json_data = json.dumps({"user": {"email": "user3@foo.com", "password": "pass"}})
        resp = self.client.post(
            url + "/register", json_data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("errors" in resp.data)
        self.assertTrue("password" in resp.data["errors"])

        #########
        # LOGIN #
        #########

        # Test login with wrong password
        json_data = json.dumps(
            {"user": {"email": "user@foo.com", "password": "wrongone"}}
        )
        resp = self.client.post(
            url + "/login", json_data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("errors" in resp.data)
        self.assertTrue("error" in resp.data["errors"])

        # Test login with wrong email
        json_data = json.dumps(
            {"user": {"email": "wrongemail@foo.com", "password": "password"}}
        )
        resp = self.client.post(
            url + "/login", json_data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("errors" in resp.data)
        self.assertTrue("error" in resp.data["errors"])

        # Test login with correct credentials
        json_data = json.dumps(
            {"user": {"email": "user2@foo.com", "password": "password"}}
        )
        resp = self.client.post(
            url + "/login", json_data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        ##################
        # LOGGED IN USER #
        ##################

        # Test getting token
        json_data = json.dumps(
            {"user": {"email": "user2@foo.com", "password": "password"}}
        )
        resp = self.client.post(
            url + "/login", json_data, content_type="application/json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in resp.data)
        token = resp.data["token"]
