from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Deal(models.Model):
    customer = models.ForeignKey(
        "users.User",
        verbose_name=_("Customer"),
        related_name="deals",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    rider = models.ForeignKey(
        "users.User",
        verbose_name=_("Rider"),
        related_name="deliveries",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    junk_point = models.ForeignKey(
        "junk.JunkPoint",
        verbose_name=_("Junk point"),
        related_name="deals",
        null=True,
        on_delete=models.SET_NULL,
    )

    date = models.DateTimeField(_("Date"), auto_now_add=True)

    description = models.TextField(_("Description"), null=True, max_length=512)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _("Deal")
        verbose_name_plural = _("Deals")
        ordering = ("id",)

    def __str__(self):
        return str(self.date)


class Trash(models.Model):
    deal = models.ForeignKey(
        "junk.Deal",
        verbose_name=_("Deal"),
        related_name="trash",
        on_delete=models.CASCADE,
    )

    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=512)

    type = models.ForeignKey(
        "junk.TrashType",
        verbose_name=_("Trash type"),
        related_name="deals",
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = _("Trash")
        verbose_name_plural = _("Trash")
        ordering = ("id",)

    def __str__(self):
        return self.name


class TrashType(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Trash type")
        verbose_name_plural = _("Trash type")
        ordering = ("id",)

    def __str__(self):
        return self.name


class JunkPoint(models.Model):
    street_name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=512)

    location = models.PointField(_("Location"))

    type = models.ForeignKey(
        "junk.JunkPointType",
        verbose_name=_("Junk point type"),
        related_name="points",
        null=True,
        on_delete=models.SET_NULL,
    )

    contract = models.ForeignKey(
        "companies.Contract",
        verbose_name=_("Contract"),
        related_name="points",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = _("Junk point")
        verbose_name_plural = _("Junk points")
        ordering = ("id",)

    def __str__(self):
        return str(self.location)


class JunkPointType(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=512)

    class Meta:
        verbose_name = _("Junk point type")
        verbose_name_plural = _("Junk point types")
        ordering = ("id",)

    def __str__(self):
        return self.name
