# Generated by Django 3.0.5 on 2020-04-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0008_microsoftteamswebhook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nachricht',
            name='aufnahmeweg',
            field=models.IntegerField(blank=True, choices=[(0, 'Fe'), (1, 'Fu'), (2, 'Me'), (3, 'Mail'), (4, 'SMS'), (5, 'Fax'), (6, 'MIS'), (7, 'drkserver')], null=True),
        ),
        migrations.AlterField(
            model_name='nachricht',
            name='befoerderungsweg',
            field=models.IntegerField(blank=True, choices=[(0, 'Fe'), (1, 'Fu'), (2, 'Me'), (3, 'Mail'), (4, 'SMS'), (5, 'Fax'), (6, 'MIS'), (7, 'drkserver')], null=True),
        ),
        migrations.AlterField(
            model_name='nachricht',
            name='richtung',
            field=models.CharField(choices=[('E', 'Eingang'), ('A', 'Ausgang'), ('R', 'Relay')], max_length=1),
        ),
    ]