from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from ecojunk.users.constants import ROL_TYPES


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    permissions = models.ManyToManyField(
        "users.Permission", verbose_name=_("Permissions")
    )
    completed_missions = models.ManyToManyField(
        "rewards.Mission", verbose_name=_("Completed missions")
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name


class Permission(models.Model):
    rol = models.CharField(_("Rol"), choices=ROL_TYPES, max_length=255)

    class Meta:
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")

    def __str__(self):
        return self.rol
