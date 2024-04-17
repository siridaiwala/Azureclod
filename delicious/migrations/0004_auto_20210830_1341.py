# Generated by Django 3.2.6 on 2021-08-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delicious', '0003_founders'),
    ]

    operations = [
        migrations.AddField(
            model_name='founders',
            name='founder_des',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='founders',
            name='founder_image',
            field=models.ImageField(blank=True, upload_to='delicious/'),
        ),
    ]
