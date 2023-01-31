from django.db import models


class CSV(models.Model):
    """Model definition for CSV."""

    # TODO: Define fields here
    csv = models.FileField()

    class Meta:
        """Meta definition for CSV."""

        verbose_name = 'CSV'
        verbose_name_plural = 'CSVs'

    def __str__(self):
        """Unicode representation of CSV."""
        pass

