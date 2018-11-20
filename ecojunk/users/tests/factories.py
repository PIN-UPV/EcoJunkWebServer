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

    @factory.post_generation
    def permissions(self, create: bool, extracted: Sequence[Any], **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for permission in extracted:
                self.permissions.add(permission)
        else:
            permission = PermissionFactory()
            self.permissions.add(permission)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["email"]


class PermissionFactory(factory.django.DjangoModelFactory):

    rol = FuzzyChoice(ROL_TYPES)

    class Meta:
        model = "users.Permission"
