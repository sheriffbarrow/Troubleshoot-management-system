from django.db import models


from django.utils.timezone import now

# Create your models here.
class Complaint(models.Model):
    room_Number = models.IntegerField(default=0)
    office_Title = models.CharField(max_length=50)
    complaint = models.CharField(max_length=100)
    additional_Info = models.TextField(max_length=50, default='unkown')
    solution = models.CharField(max_length=100)
    occurance = models.IntegerField(default=0)
    date = models.DateField(default=now, editable=False)
