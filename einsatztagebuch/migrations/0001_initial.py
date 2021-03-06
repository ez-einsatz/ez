# Generated by Django 3.0.5 on 2020-04-20 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nachrichten', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Einsatztagebucheintrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField(blank=True, null=True)),
                ('massnahme', models.TextField(blank=True, null=True)),
                ('nachricht', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='nachrichten.Nachricht')),
            ],
            options={
                'verbose_name': 'Einsatztagebucheintrag',
                'verbose_name_plural': 'Einsatztagebucheinträge',
            },
        ),
    ]
