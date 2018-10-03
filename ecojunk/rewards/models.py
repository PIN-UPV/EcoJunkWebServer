from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _


class Mission(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=512)
    dificulty = models.IntegerField(
        _("dificulty"), validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    badges = models.ManyToManyField("rewards.Badge", verbose_name=_("Badges"))

    class Meta:
        verbose_name = _("Mission")
        verbose_name = _("Missions")

    def __str__(self):
        return self.name


class Badge(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=512)

    class Meta:
        verbose_name = _("Badge")
        verbose_name = _("Badges")

    def __str__(self):
        return self.name
