# Generated by Django 4.2 on 2023-09-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_villa_room_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villa',
            name='description',
            field=models.CharField(default='My New Villa', max_length=500),
        ),
    ]
