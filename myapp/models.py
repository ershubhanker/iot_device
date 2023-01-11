from django.db import models

time_stamp = (
     ("AM", "AM"),
    ("PM", "PM"),
)

channel = (
     ("A", "A"),
    ("B", "B"),
)

sensed_panel_rating_choice = (
     ("50", "50"),
    ("100", "100"),
    ("200", "200"),
    ("400", "400")
)

circuit_breaker = (
     ("0", "0"),
    ("15", "15"),
    ("20", "20"),
    ("30", "30"),
    ("40", "40"),
    ("50", "50"),
    ("60", "60"),
    ("70", "70"),
    ("80", "80"),
    ("100", "100")
)


class WifiDetails(models.Model):
    ssid = models.CharField(max_length=30, editable=True)
    password = models.CharField(max_length=30, editable=True)
    


class DateTimeDetails(models.Model):
    _date = models.DateField(null=True, editable=True)
    _time = models.TimeField(null=True, editable=True)
    am_pm = models.CharField(max_length=30,choices = time_stamp,default='AM')
    timezone = models.CharField(max_length=30)
    


class lockoutDetails(models.Model):
    weekday1 = models.CharField(max_length=30)
    weekday2 = models.CharField(max_length=30)
    weekend1 = models.CharField(max_length=30)
    weekend2 = models.CharField(max_length=30)
    

class ECDetails(models.Model):
    id = models.AutoField(primary_key=True)
    sensed_panel_rating = models.CharField(max_length=30,choices = sensed_panel_rating_choice,default='50')
    sensor_ct_rating = models.CharField(max_length=30,choices = sensed_panel_rating_choice,default='200')
    circuit_breaker_a = models.CharField(max_length=30,choices = circuit_breaker,default='15')
    circuit_breaker_b = models.CharField(max_length=30,choices = circuit_breaker,default='15')

    c1 = models.CharField(max_length=30,null=True)
    max_amp1 = models.IntegerField(null=True)
    c1ab = models.CharField(max_length=30,choices = channel,default='A')
    c2 = models.CharField(max_length=30,null=True)
    max_amp2 = models.IntegerField(null=True)
    c2ab = models.CharField(max_length=30,null=True,choices = channel,default='A')
    c3 = models.CharField(max_length=30,null=True)
    max_amp3 = models.IntegerField(null=True)
    c3ab = models.CharField(max_length=30,null=True,choices = channel,default='A')
    c4 = models.CharField(max_length=30,null=True)
    max_amp4 = models.IntegerField(null=True)
    c4ab = models.CharField(max_length=30,null=True,choices = channel,default='A')
    
