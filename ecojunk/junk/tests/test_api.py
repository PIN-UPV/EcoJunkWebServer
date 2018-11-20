from rest_framework import status
from rest_framework.test import APITestCase

from ecojunk.junk.models import Deal, JunkPoint
from ecojunk.junk.tests.factories import (
    DealFactory,
    JunkPointFactory,
    JunkPointTypeFactory,
    JunkPointRealisticFactory,
)
from ecojunk.junk.api.v1.serializers import JunkPointSerializer
from ecojunk.users.constants import RIDER, USER
from ecojunk.users.tests.factories import PermissionFactory, UserFactory
from django.contrib.gis.geos import Point


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

    def test_list_junk_points_with_coords(self):
        junk_point = JunkPointRealisticFactory()
        location = Point(39.478_328_1, -0.376_823_7)
        self.client.force_authenticate(self.user)
        response = self.client.get(
            f"/api/v1/junk_points/?lat={location[1]}&lng={location[0]}", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        serializer = JunkPointSerializer(junk_point)
        self.assertTrue(serializer.data in data["results"])

    def test_create_junk_point(self):
        point_types = JunkPointTypeFactory.create_batch(size=3)
        data = {
            "street_name": "Junk point street name",
            "description": "Junk point description",
            "location": "POINT (2.2945 48.8583)",
            "types": [point_types[0].pk, point_types[1].pk, point_types[2].pk],
        }

        self.client.force_authenticate(self.user)
        response = self.client.post("/api/v1/junk_points/", data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JunkPoint.objects.count(), 1)


class DealTest(APITestCase):
    deal_factory = JunkPointFactory

    def setUp(self):
        self.user_rider = UserFactory()
        self.user_customer = UserFactory()

        self.rol_rider = PermissionFactory(rol=RIDER)
        self.rol_customer = PermissionFactory(rol=USER)

        self.user_rider.permissions.add(self.rol_rider)
        self.user_rider.save()

        self.user_customer.permissions.add(self.rol_customer)
        self.user_customer.save()

    def test_list_deal(self):
        deals = DealFactory.create_batch(size=10)

        self.client.force_authenticate(self.user_customer)
        response = self.client.get("/api/v1/deals/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(deals), data["count"])

    def test_create_deal(self):
        junk_point = JunkPointFactory()
        data = {"junk_point": junk_point.pk, "price": 2.0, "junk": "Microwave"}

        self.client.force_authenticate(self.user_customer)
        response = self.client.post("/api/v1/deals/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Deal.objects.count(), 1)
        self.assertIn("Microwave", response.json()["junk"])

    def test_accept_deal(self):
        deal = DealFactory()
        deal.rider = None
        deal.save()

        self.client.force_authenticate(self.user_rider)
        response = self.client.post(f"/api/v1/deals/{deal.pk}/accept_deal/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Deal.objects.get(pk=deal.pk).rider == self.user_rider)

    def test_decline_deal(self):
        deal = DealFactory()

        deal.rider = self.user_rider
        deal.save()

        self.client.force_authenticate(self.user_rider)
        response = self.client.post(f"/api/v1/deals/{deal.pk}/decline_deal/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
