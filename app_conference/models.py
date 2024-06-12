from django.db import models


class ConferenceDaysModel(models.Model):
    day_number = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.day_number)


class ConferenceAgendaModel(models.Model):
    title = models.CharField(max_length=255)
    oclock = models.CharField(max_length=30)
    day_id = models.ForeignKey(ConferenceDaysModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'conference_agenda'
        verbose_name_plural = 'Conference Agenda'


class SponsorPartnersModel(models.Model):
    image = models.ImageField(upload_to='sponsor_and_partners/%y/%m/%d/')

    def __str__(self):
        return self.image.name

    class Meta:
        db_table = 'sponsor_partners'
        verbose_name_plural = 'Sponsor and Partners'
