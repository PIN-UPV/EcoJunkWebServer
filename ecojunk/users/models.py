from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ecojunk.users.constants import ROL_TYPES


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    permissions = models.ManyToManyField(
        "users.Permission", verbose_name=_("permissions")
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name


class Permission(mode):
    rol = models.CharField(_("Rol"), choices=ROL_TYPES, max_length=255)

    class Meta:
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")

    def __str__(self):
        return self.rol
