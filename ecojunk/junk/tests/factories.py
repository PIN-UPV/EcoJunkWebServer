import factory
from django.utils.text import slugify
from factory.fuzzy import FuzzyInteger, FuzzyText

from ecojunk.core.tests.fuzzy import FuzzyPoint


class JunkPointTypeFactory(factory.django.DjangoModelFactory):
    name = FuzzyText()
    description = FuzzyText()

    class Meta:
        model = "junk.JunkPointType"


class JunkPointFactory(factory.django.DjangoModelFactory):
    location = FuzzyPoint()
    type = factory.SubFactory(JunkPointTypeFactory)

    class Meta:
        model = "junk.JunkPoint"
