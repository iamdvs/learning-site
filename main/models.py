from django.db import models
import datetime
from django.contrib.auth.models import User

class Series(models.Model):

    teacher1,teacher2,teacher3='davod vesaghati','mohamad','ali'
    teacher_choices=[
        (teacher1,'Davod Vesaghati'),
        (teacher2,'mohammad khodayi'),
        (teacher3,'ali mohammadi'),
    ]

    issue=models.CharField(max_length=30)
    explanation=models.TextField(max_length=2000)
    series_photo=models.ImageField(upload_to='images/',default='no-img.jpg',blank=True)
    teacher=models.CharField(max_length=40,choices=teacher_choices,default=teacher1)
    create_date=models.DateTimeField(auto_now=True)
    links=models.URLField(blank=True)


    class Meta:
        ordering=('create_date',)

    def __str__(self):
        return self.issue
    
