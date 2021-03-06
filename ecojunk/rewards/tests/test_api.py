from rest_framework import status
from rest_framework.test import APITestCase
from test_plus import TestCase

from ecojunk.rewards.tests.factories import BadgeFactory, MissionFactory
from ecojunk.users.tests.factories import UserFactory


class MissionResourceTest(APITestCase):
    mission_factory = MissionFactory

    def setUp(self):
        self.user = UserFactory()

    def test_list_missions(self):
        missions = MissionFactory.create_batch(size=10)

        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/missions/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(missions), data["count"])


class BadgeResourceTest(APITestCase):
    badge_factory = BadgeFactory

    def setUp(self):
        self.user = UserFactory()

    def test_list_badges(self):
        badges = BadgeFactory.create_batch(size=10)

        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/badges/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(badges), data["count"])
