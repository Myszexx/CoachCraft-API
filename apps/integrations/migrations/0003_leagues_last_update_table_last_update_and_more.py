# Generated by Django 5.2b1 on 2025-03-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0002_table_team_name_table_team_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='leagues',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zpns',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
