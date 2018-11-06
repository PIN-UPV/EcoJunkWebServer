from typing import Any, Sequence

import factory
from django.contrib.auth import get_user_model
from factory.fuzzy import FuzzyChoice

from ecojunk.users.constants import ROL_TYPES


class UserFactory(factory.django.DjangoModelFactory):

    email = factory.Faker("email")
    name = factory.Faker("name")

    @factory.post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = factory.Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["email"]


class RolFactory(factory.django.DjangoModelFactory):

    rol = FuzzyChoice(ROL_TYPES)

    class Meta:
        model = "users.Permission"
