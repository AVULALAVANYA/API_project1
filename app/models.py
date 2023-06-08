from django.db import models

# Create your models here.
class Emplayee(models.Model):
    ename=models.CharField(max_length=100)
    eid=models.IntegerField(primary_key=True)
    eage=models.IntegerField()
