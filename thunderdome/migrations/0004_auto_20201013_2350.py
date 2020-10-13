# Generated by Django 2.2.16 on 2020-10-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thunderdome', '0003_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='wordcount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
