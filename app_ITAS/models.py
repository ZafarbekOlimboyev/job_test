from django.db import models


class GenderModel(models.Model):
    gender = models.CharField(max_length=25)

    def __str__(self):
        return self.gender

    class Meta:
        db_table = 'genders'
        verbose_name_plural = 'Genders'


class CommitteeGroupModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'committees'
        verbose_name_plural = 'Committees'


class PositionsModel(models.Model):
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.position

    class Meta:
        db_table = 'positions'
        verbose_name_plural = 'Position'


class UniversitiesModel(models.Model):
    university_name = models.CharField(max_length=255)

    def __str__(self):
        return self.university_name

    class Meta:
        db_table = 'universities'
        verbose_name_plural = 'Universities'


class CommitteeModel(models.Model):
    name = models.CharField(max_length=255)
    position_id = models.ForeignKey(PositionsModel, on_delete=models.CASCADE)
    committee_group_id = models.ForeignKey(CommitteeGroupModel, on_delete=models.CASCADE)
    gender_id = models.ForeignKey(GenderModel, on_delete=models.CASCADE)
    university_id = models.ForeignKey(UniversitiesModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='committee_images/%y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'committee'
        verbose_name_plural = 'Committee'


class SpeakersModel(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=765)
    image = models.ImageField(upload_to='speakers_images/%y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'speakers'
        verbose_name_plural = 'Speakers'
