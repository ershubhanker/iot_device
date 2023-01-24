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
    ("15", "15"),
    ("20", "20"),
    ("30", "30"),
    ("40", "40"),
    ("50", "50"),
    ("60", "60"),
    ("70", "70"),
    ("80", "80"),
    ("90", "90"),
    ("100", "100")
)

# https://www.djangosnippets.org/snippets/2703/
TIME_ZONE_CHOICES = (
     ('-12.0', '(GMT -12:00) Eniwetok, Kwajalein'),
     ('-11.0', '(GMT -11:00) Midway Island, Samoa'),
     ('-10.0', '(GMT -10:00) Hawaii'),
     ('-9.0', '(GMT -9:00) Alaska'),
     ('-8.0', '(GMT -8:00) Pacific Time (US &amp; Canada)'),
     ('-7.0', '(GMT -7:00) Mountain Time (US &amp; Canada)'),
     ('-6.0', '(GMT -6:00) Central Time (US &amp; Canada), Mexico City'),
     ('-5.0', '(GMT -5:00) Eastern Time (US &amp; Canada), Bogota, Lima'),
     ('-4.0', '(GMT -4:00) Atlantic Time (Canada), Caracas, La Paz'),
     ('-3.5', '(GMT -3:30) Newfoundland'),
     ('-3.0', '(GMT -3:00) Brazil, Buenos Aires, Georgetown'),
     ('-2.0', '(GMT -2:00) Mid-Atlantic'),
     ('-1.0', '(GMT -1:00 hour) Azores, Cape Verde Islands'),
     ('0.0', '(GMT) Western Europe Time, London, Lisbon, Casablanca'),
     ('1.0', '(GMT +1:00 hour) Brussels, Copenhagen, Madrid, Paris'),
     ('2.0', '(GMT +2:00) Kaliningrad, South Africa'),
     ('3.0', '(GMT +3:00) Baghdad, Riyadh, Moscow, St. Petersburg'),
     ('3.5', '(GMT +3:30) Tehran'),
     ('4.0', '(GMT +4:00) Abu Dhabi, Muscat, Baku, Tbilisi'),
     ('4.5', '(GMT +4:30) Kabul'),
     ('5.0', '(GMT +5:00) Ekaterinburg, Islamabad, Karachi, Tashkent'),
     ('5.5', '(GMT +5:30) Bombay, Calcutta, Madras, New Delhi'),
     ('5.75', '(GMT +5:45) Kathmandu'),
     ('6.0', '(GMT +6:00) Almaty, Dhaka, Colombo'),
     ('7.0', '(GMT +7:00) Bangkok, Hanoi, Jakarta'),
     ('8.0', '(GMT +8:00) Beijing, Perth, Singapore, Hong Kong'),
     ('9.0', '(GMT +9:00) Tokyo, Seoul, Osaka, Sapporo, Yakutsk'),
     ('9.5', '(GMT +9:30) Adelaide, Darwin'),
     ('10.0', '(GMT +10:00) Eastern Australia, Guam, Vladivostok'),
     ('11.0', '(GMT +11:00) Magadan, Solomon Islands, New Caledonia'),
     ('12.0', '(GMT +12:00) Auckland, Wellington, Fiji, Kamchatka')
)

class WifiDetails(models.Model):
    ssid = models.CharField(max_length=30,null=True, editable=True)
    password = models.CharField(max_length=30,null=True, editable=True)
    


class DateTimeDetails(models.Model):
    date = models.DateField(null=True, editable=True)
    local_time = models.TimeField(null=True, editable=True)
    # am_pm = models.CharField(max_length=30,choices = time_stamp,default='AM')
    timezone = models.CharField(max_length=30,choices=TIME_ZONE_CHOICES)
    


class lockoutDetails(models.Model):
    weekday_from_1 = models.CharField(max_length=30,null=True,blank=True)
    weekday_to_1 = models.CharField(max_length=30,null=True,blank=True)
    weekday_from_2 = models.CharField(max_length=30,null=True,blank=True)
    weekday_to_2 = models.CharField(max_length=30,null=True,blank=True)

    weekend_from_1 = models.CharField(max_length=30,null=True,blank=True)
    weekend_to_1 = models.CharField(max_length=30,null=True,blank=True)
    weekend_from_2 = models.CharField(max_length=30,null=True,blank=True)
    weekend_to_2 = models.CharField(max_length=30,null=True,blank=True)

    

class ECDetails(models.Model):
    id = models.AutoField(primary_key=True)
    sensed_panel_rating = models.CharField(max_length=30,choices = sensed_panel_rating_choice,default='100')
    sensor_ct_rating = models.CharField(max_length=30,choices = sensed_panel_rating_choice,default='200')
    circuit_breaker_a = models.CharField(max_length=30,choices = circuit_breaker,default='40')
    circuit_breaker_b = models.CharField(max_length=30,choices = circuit_breaker,default='15')

    c1 = models.CharField(max_length=30,null=True, default='A')
    max_amp1 = models.IntegerField(null=True,default=0)
    c1_circuit = models.CharField(max_length=30,choices = channel,default='A')
    c2 = models.CharField(max_length=30,null=True)
    max_amp2 = models.IntegerField(null=True,default=0)
    c2_circuit = models.CharField(max_length=30,null=True,choices = channel,default='A')
    c3 = models.CharField(max_length=30,null=True)
    max_amp3 = models.IntegerField(null=True,default=0)
    c3_circuit = models.CharField(max_length=30,null=True,choices = channel,default='A')
    c3 = models.CharField(max_length=30,null=True)
    max_amp4 = models.IntegerField(null=True,default=0)
    c4_circuit = models.CharField(max_length=30,null=True,choices = channel,default='A')
    
