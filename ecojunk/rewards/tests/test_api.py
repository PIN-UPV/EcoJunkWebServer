from rest_framework import status
from test_plus import TestCase

from ecojunk.rewards.models import Mission, Badge
from ecojunk.rewards.tests.factories import MissionFactory, BadgeFactory
from ecojunk.users.tests.factories import UserFactory


class MissionResourceTest(TestCase):
    mission_factory = MissionFactory

    def setUp(self):
        self.user = UserFactory()

    def test_list_missions(self):
        missions = MissionFactory.create_batch(size=10)
        response = self.client.get("/api/v1/missions/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(missions), data["count"])

    def test_create_mission(self):
        badge = BadgeFactory()
        data = {
            "name": "new missions",
            "description": "That's a new mission",
            "dificulty": 1,
            "badges": [badge.pk],
        }
        response = self.client.post("/api/v1/missions/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Badge.objects.count(), 1)


class BadgeResourceTest(TestCase):
    badge_factory = BadgeFactory

    def setUp(self):
        self.user = UserFactory()

    def test_list_badges(self):
        badges = BadgeFactory.create_batch(size=10)
        response = self.client.get("/api/v1/badges/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(badges), data["count"])


