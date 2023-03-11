from django.db import models
from django.utils.translation import gettext_lazy as _


class Competition(models.Model):
    name = models.CharField(
        max_length=100,
        help_text = _('Format: required, max-length:100')
    )
    description = models.TextField(
        max_length=500,
        null = True,
        blank = True,
        help_text = _('Format: optional, max-length:500')
    )
    target = models.IntegerField(
        default = 0,
        help_text = _('Competition target points')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(
        help_text = _('Competition start date'),
    )
    end_date = models.DateField(
        help_text = _('Competition end date'),
    )

    def __str__(self):
        return self.name