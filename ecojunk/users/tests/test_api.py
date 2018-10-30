from rest_framework import status
from rest_framework.test import APITestCase

from ecojunk.users.tests.factories import UserFactory


class UserAuthenticationTest(APITestCase):
    def setUp(self):
        self.user = UserFactory(email="user@foo.com")
        self.user.set_password("password")
        self.user.save()

        self.url = "/api/v1/users"

    def test_register(self):
        # Test register user with existing username
        data = {"email": "user@foo.com", "password": "password"}
        response = self.client.post(f"{self.url}/register/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("error" in response.data)

        # Test register user with new username
        data = {"email": "user2@foo.com", "password": "password"}
        response = self.client.post(f"{self.url}/register/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("email" in response.data)
        self.assertTrue("token" in response.data)

        # Test register user with weak password
        data = {"email": "user3@foo.com", "password": "pass"}
        response = self.client.post(f"{self.url}/register/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("errors" in response.data)
        self.assertTrue("password" in response.data["errors"])

    def test_login(self):
        # Test login with wrong password
        data = {"email": "user@foo.com", "password": "wrongone"}
        response = self.client.post(f"{self.url}/login/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("error" in response.data)

        # Test login with wrong email
        data = {"email": "wrongemail@foo.com", "password": "password"}
        response = self.client.post(f"{self.url}/login/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("error" in response.data)

        # Test login with correct credentials
        data = {"email": "user@foo.com", "password": "password"}
        response = self.client.post(f"{self.url}/login/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        # Test getting token
        self.client.force_authenticate(self.user)
        response = self.client.get(f"{self.url}/me/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.data)
