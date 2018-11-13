import factory
<<<<<<< HEAD
from factory.fuzzy import FuzzyText, FuzzyFloat
=======
from factory.fuzzy import FuzzyText
>>>>>>> 7e77ea6cc01cffbd9576a6baedbe3ce98aec8034
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
<<<<<<< HEAD
        median = Point(39.4783281, -0.3768237)
=======
        median = Point(-0.3768237, 39.4783281)
>>>>>>> 7e77ea6cc01cffbd9576a6baedbe3ce98aec8034
        std = 0.02

    @factory.lazy_attribute
    def location(self):
        return ValenciaPoint(self.median, self.std).fuzz()

    class Meta:
        model = "junk.JunkPoint"
<<<<<<< HEAD
        exclude = ("median", "std")
=======
        exclude = ('median', 'std',)
>>>>>>> 7e77ea6cc01cffbd9576a6baedbe3ce98aec8034


class DealFactory(factory.django.DjangoModelFactory):
    customer = factory.SubFactory("users.tests.factories.UserFactory")
    rider = factory.SubFactory("users.tests.factories.UserFactory")
    junk_point = factory.SubFactory("junk.tests.factories.JunkPointFactory")
    price = FuzzyFloat(low=1, high=9999.99)

    class Meta:
        model = "junk.Deal"
