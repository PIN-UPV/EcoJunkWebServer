from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    promoted = models.BooleanField(_("promoted"), default=False)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
        ordering = ("id",)

    def __str__(self):
        return self.name


class Contract(models.Model):
    company = models.ForeignKey(
        "companies.Company",
        verbose_name=_("Company"),
        related_name="contracts",
        on_delete=models.CASCADE,
    )

    end_date = models.DateTimeField(_("End date"))

    class Meta:
        verbose_name = _("Contract")
        verbose_name_plural = _("Contracts")
        ordering = ("id",)

    def __str__(self):
        return self.name
