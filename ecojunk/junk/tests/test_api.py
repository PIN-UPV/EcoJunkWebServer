from rest_framework import status
from rest_framework.test import APITestCase
from test_plus import TestCase

from ecojunk.junk.models import Deal, JunkPoint
from ecojunk.junk.tests.factories import (DealFactory, JunkPointFactory,
                                          JunkPointTypeFactory)
from ecojunk.users.tests.factories import UserFactory


class JunkPointTypeResourceTest(APITestCase):
    junk_point_type_factory = JunkPointTypeFactory

    def setUp(self):
        self.user = UserFactory()

    def test_list_junk_point_types(self):
        junk_point_types = JunkPointTypeFactory.create_batch(size=10)

        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/junk_point_types/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(junk_point_types), data["count"])


class JunkPointResourceTest(APITestCase):
    junk_point_factory = JunkPointFactory

    def setUp(self):
        self.user = UserFactory()

    def test_list_junk_points(self):
        junk_points = JunkPointFactory.create_batch(size=10)

        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/junk_points/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(junk_points), data["count"])

    def test_create_junk_point(self):
        point_type = JunkPointTypeFactory()
        data = {
            "street_name": "Junk point street name",
            "description": "Junk point description",
            "location": "POINT (12.492324113849 41.890307434153)",
            "type": point_type.pk,
        }

        self.client.force_authenticate(self.user)
        response = self.client.post("/api/v1/junk_points/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JunkPoint.objects.count(), 1)


class DealTest(APITestCase):
    deal_factory = JunkPointFactory

    def setUp(self):
        self.user = UserFactory()

    def test_list_deal(self):
        deals = DealFactory.create_batch(size=10)

        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/deals/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(deals), data["count"])

    def test_create_deal(self):
        junk_point = JunkPointFactory()
        data = {"junk_point": junk_point.pk}

        self.client.force_authenticate(self.user)
        response = self.client.post("/api/v1/deals/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Deal.objects.count(), 1)
