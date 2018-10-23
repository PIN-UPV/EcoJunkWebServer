import factory
from factory.fuzzy import FuzzyInteger, FuzzyText


class BadgeFactory(factory.django.DjangoModelFactory):
    name = FuzzyText()
    description = FuzzyText()

    class Meta:
        model = "rewards.Badge"


class MissionFactory(factory.django.DjangoModelFactory):
    name = FuzzyText()
    description = FuzzyText()
    difficulty = FuzzyInteger(10)
    badges = factory.SubFactory(BadgeFactory)

    @factory.post_generation
    def badges(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for badge in extracted:
                self.badges.add(badge)

    class Meta:
        model = "rewards.Mission"
