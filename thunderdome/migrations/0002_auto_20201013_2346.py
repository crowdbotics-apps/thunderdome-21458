# Generated by Django 2.2.16 on 2020-10-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thunderdome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='closedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prompt',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prompt',
            name='wordcount',
            field=models.PositiveSmallIntegerField(blank=True, max_length=256, null=True),
        ),
    ]
