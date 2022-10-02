from django.db import models

# Create your models here.

# Create your models here.
class COVID_REGION(models.Model):
    REGDATE = models.CharField(max_length=8)
    REGION = models.CharField(max_length=6)
    REGCASE = models.IntegerField()
    REGDEATH = models.IntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["REGDATE", "REGION"], name="region-unique")]
        db_table = 'COVID_REGION'

class COVID_DOMESTIC(models.Model):
    COVDATE = models.CharField(max_length=8, primary_key=True)
    DAILY_CASE = models.IntegerField()
    TOTAL_CASE = models.IntegerField()
    DAILY_DEATH = models.IntegerField()

    class Meta:
        db_table = 'COVID_DOMESTIC'