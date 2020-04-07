# Generated by Django 3.0.5 on 2020-04-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Einheit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('taktisches_zeichen', models.FileField(upload_to='media/einheiten/taktisches_zeichen/')),
            ],
            options={
                'verbose_name': 'Einheit',
                'verbose_name_plural': 'Einheiten',
            },
        ),
    ]
