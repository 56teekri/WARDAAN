# Generated by Django 3.1.1 on 2021-06-27 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='url',
            field=models.URLField(default='https://www.imsanz.org.au/about-us/what-is-a-general-physician', max_length=250),
        ),
    ]
