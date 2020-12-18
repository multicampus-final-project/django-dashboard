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
    machine_id = models.IntegerField(default=0)

class Partner(models.Model):
    manager = models.CharField(max_length=30)
    email = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    message_confirmation = models.BooleanField()
    tel = models.CharField(max_length=30, default="000-0000-0000")


class Machine(models.Model):
    partner = models.ForeignKey("Partner", related_name="m_partner", db_column="partner_id", on_delete=models.SET_NULL, null=True)
    local1 = models.CharField(max_length=100)
    local2 = models.CharField(max_length=100)
    class1_full_rate = models.IntegerField(default=0)
    class2_full_rate = models.IntegerField(default=0)
    class3_full_rate = models.IntegerField(default=0)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)
    name = models.CharField(max_length=50, default="")

class Collection(models.Model):
    machine = models.ForeignKey("Machine", related_name="machine_id", db_column="machine_id", on_delete=models.SET_NULL, null=True)
    partner = models.ForeignKey("Partner", related_name="partner", db_column="machine", on_delete=models.SET_NULL, null=True)
    collected_date = models.DateTimeField(auto_now_add=True)
    class1_amount = models.IntegerField(default=0)
    class2_amount = models.IntegerField(default=0)
    class3_amount = models.IntegerField(default=0)
