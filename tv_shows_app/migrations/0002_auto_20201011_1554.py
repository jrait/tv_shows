# Generated by Django 2.2.4 on 2020-10-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateField(),
        ),
    ]
