# Generated by Django 3.0.5 on 2020-04-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0004_mail_verteiler'),
    ]

    operations = [
        migrations.AddField(
            model_name='nachricht',
            name='erstellungszeit',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
