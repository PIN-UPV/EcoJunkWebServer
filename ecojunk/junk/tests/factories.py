import factory
from factory.fuzzy import FuzzyText
from ecojunk.core.tests.fuzzy import FuzzyPoint, ValenciaPoint
from django.contrib.gis.geos import Point


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


class JunkPointRealisticFactory(factory.django.DjangoModelFactory):
    street_name = FuzzyText()
    description = FuzzyText()
    type = factory.SubFactory("junk.tests.factories.JunkPointTypeFactory")

    class Params:
        median = Point(39.4783281, -0.3768237)
        std = 0.02

    @factory.lazy_attribute
    def location(self):
        return ValenciaPoint(self.median, self.std).fuzz()

    class Meta:
        model = "junk.JunkPoint"
        exclude = ('median', 'std',)


class DealFactory(factory.django.DjangoModelFactory):
    customer = factory.SubFactory("users.tests.factories.UserFactory")
    rider = factory.SubFactory("users.tests.factories.UserFactory")
    junk_point = factory.SubFactory("junk.tests.factories.JunkPointFactory")

    class Meta:
        model = "junk.Deal"
