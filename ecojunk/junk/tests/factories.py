import factory
from factory.fuzzy import FuzzyText

from ecojunk.core.tests.fuzzy import FuzzyPoint


class JunkPointTypeFactory(factory.django.DjangoModelFactory):
    name = FuzzyText()
    description = FuzzyText()

    class Meta:
        model = "junk.JunkPointType"


class JunkPointFactory(factory.django.DjangoModelFactory):
    street_name = FuzzyText()
    description = FuzzyText()
    location = FuzzyPoint()
    type = factory.SubFactory("junk.tests.factories.JunkPointTypeFactory")

    class Meta:
        model = "junk.JunkPoint"


class DealFactory(factory.django.DjangoModelFactory):
    customer = factory.SubFactory("users.tests.factories.UserFactory")
    rider = factory.SubFactory("users.tests.factories.UserFactory")
    junk_point = factory.SubFactory("junk.tests.factories.JunkPointFactory")

    class Meta:
        model = "junk.Deal"
