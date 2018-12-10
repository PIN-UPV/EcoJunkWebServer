import factory
from factory.fuzzy import FuzzyText, FuzzyFloat, FuzzyChoice
from ecojunk.core.tests.fuzzy import FuzzyPoint, ValenciaPoint
from django.contrib.gis.geos import Point
from ecojunk.junk.constants import TYPES
import random


class JunkPointTypeFactory(factory.django.DjangoModelFactory):
    name = FuzzyChoice(TYPES)
    description = FuzzyText()

    class Meta:
        model = "junk.JunkPointType"


class JunkPointFactory(factory.django.DjangoModelFactory):
    street_name = FuzzyText()
    description = "" #  FuzzyText()
    location = FuzzyPoint()

    @factory.post_generation
    def types(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for type_ in extracted:
                self.types.add(type_)
                self.description += type_.name + " "

    class Meta:
        model = "junk.JunkPoint"


class JunkPointRealisticFactory(factory.django.DjangoModelFactory):
    street_name = FuzzyText()
    description = "" # FuzzyText()

    @factory.post_generation
    def types(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for type_ in extracted:
                self.types.add(type_)
                self.description += type_.name + " "

    class Params:
        median = Point(39.4783281, -0.3768237)
        std = 0.02

    @factory.lazy_attribute
    def location(self):
        return ValenciaPoint(self.median, self.std).fuzz()

    class Meta:
        model = "junk.JunkPoint"
        exclude = ("median", "std")


class DealFactory(factory.django.DjangoModelFactory):
    junk = FuzzyText()
    customer = factory.SubFactory("users.tests.factories.UserFactory")
    rider = factory.SubFactory("users.tests.factories.UserFactory")
    price = FuzzyFloat(low=1, high=9999.99)

    class Meta:
        model = "junk.Deal"
