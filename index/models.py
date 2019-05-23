from django.db import models

# Create your models here.

class Series(models.Model):

    teacher1,teacher2,teacher3='da','mo','ali'
    teacher_choices=[
        (teacher1,'Davod Vesaghati'),
        (teacher2,'mohammad khodayi'),
        (teacher3,'ali mohammadi'),
    ]

    issue=models.CharField(max_length=30)
    explanation=models.TextField(max_length=2000)
    series_photo=models.ImageField(upload_to='images/',default='no-img.jpg',blank=True)
    teacher=models.CharField(max_length=2,choices=teacher_choices,default=teacher1)


    def __str__(self):
        return self.issue
    