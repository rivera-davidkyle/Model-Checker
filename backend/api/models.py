from django.db import models
import hashlib

class CSV(models.Model):
    """Model definition for CSV."""

    # TODO: Define fields here
    csv = models.FileField(upload_to='./csv')
    hash = models.CharField(max_length=40, unique=True, blank=True)
    class Meta:
        """Meta definition for CSV."""
        verbose_name = 'CSV'
        verbose_name_plural = 'CSVs'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.csv:
            with self.csv.open(mode='rb') as file:
                contents = file.read()
                sha1 = hashlib.sha1(contents)
                self.hash = sha1.hexdigest()
        super().save(*args, **kwargs)


"""
class PredModel(models.Model):

    # TODO: Define fields here
    csv = models.ForeignKey(CSV, on_delete=models.CASCADE)
    target_feature = models.CharField(max_length=40, blank=True)
    auc = models.IntegerField()
    model = models.CharField(max_length=40, blank=True)
    param = models.CharField(max_length=100, blank=True)
    class Meta:
        verbose_name = 'PredModel'
        verbose_name_plural = 'PredModels'"""





    

