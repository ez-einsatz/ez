# Generated by Django 3.0.5 on 2020-04-09 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nachrichten', '0007_nachricht_sichtungsvermerk'),
    ]

    operations = [
        migrations.CreateModel(
            name='MicrosoftTeamsWebhook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webhook_url', models.CharField(max_length=200, verbose_name='Microsoft Teams Webhook URL')),
                ('funktion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='funktionen', related_query_name='funktion', to='nachrichten.Funktion', verbose_name='Funktion')),
            ],
            options={
                'verbose_name': 'Microsoft Teams Webhook',
                'verbose_name_plural': 'Microsoft Teams Webhooks',
            },
        ),
    ]
