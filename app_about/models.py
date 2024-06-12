from django.db import models


class AboutModel(models.Model):
    conference_coordinator = models.JSONField()
    phone_numbers = models.JSONField()
    emails = models.JSONField()
    location = models.CharField(max_length=765)

    def __str__(self):
        return self.location

    class Meta:
        db_table = 'about'
        verbose_name_plural = "About"
