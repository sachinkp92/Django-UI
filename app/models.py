"""from django.db import models

sendsms = (('immediately', 'Immediately'),
              ('Start sending SMS at', 'Start sending SMS at'))
# Create your models here.
class Sender(models.Model):
    smsfrom = models.CharField(max_length=10)
    smstext = models.TextField(max_length=200)
    recipients = models.IntegerField(max_length=200)
    sendsms = models.ChoiceField(max_length=10,choices=sendsms,default='user')"""



