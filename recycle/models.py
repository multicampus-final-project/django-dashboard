from django.db import models
from django.utils import timezone


# Create your models here.
class RUser(models.Model):
    rfid = models.CharField(max_length=30, primary_key=True)
    nickname = models.CharField(max_length=10)
    pw = models.CharField(max_length=20)
    total_point = models.IntegerField()


class BottleClass(models.Model):
    bottle_class = models.IntegerField(primary_key=True)
    recycle_class = models.IntegerField()
    point = models.IntegerField(default=0)


class Bottle(models.Model):
    rUser = models.ForeignKey("RUser", related_name="r_user", db_column="user_rfid", on_delete=models.SET_NULL, null=True)
    bottle_c = models.ForeignKey(BottleClass, related_name="b_class", db_column="bottle_class", on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    datetime = models.DateTimeField(default=timezone.now)



