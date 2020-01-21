# Generated by Django 3.0.2 on 2020-01-20 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='<built-in function id>', max_length=32),
        ),
        migrations.AddField(
            model_name='game',
            name='numberoftries',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='play',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
