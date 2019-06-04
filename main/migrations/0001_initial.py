# Generated by Django 2.2.1 on 2019-06-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=30)),
                ('explanation', models.TextField(max_length=2000)),
                ('series_photo', models.ImageField(blank=True, default='no-img.jpg', upload_to='images/')),
                ('teacher', models.CharField(choices=[('davod vesaghati', 'Davod Vesaghati'), ('mohamad', 'mohammad khodayi'), ('ali', 'ali mohammadi')], default='davod vesaghati', max_length=40)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('links', models.URLField(blank=True)),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='NewFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
