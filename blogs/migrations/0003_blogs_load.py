# Generated by Django 3.1.1 on 2021-07-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210703_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='load',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
