from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

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
    
class Articles(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail',kwargs={'pk':self.pk})    
    
