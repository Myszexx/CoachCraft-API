# Generated by Django 5.1.3 on 2025-03-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='team_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='team_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
