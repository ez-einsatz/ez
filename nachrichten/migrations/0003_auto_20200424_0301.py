# Generated by Django 3.0.5 on 2020-04-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0002_auto_20200421_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='aufnahmevermerk',
            name='kanal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='befoerderungsvermerk',
            name='kanal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
