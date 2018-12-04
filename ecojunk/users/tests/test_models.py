from django.test import TestCase
from ecojunk.users.models import User
from ecojunk.users.constants import USER


class UserAuthenticationTest(TestCase):
    def test_create_user_set_permission(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="12345")
        permission = user.permissions.filter(rol=USER).first()
        self.assertIsNotNone(permission)
