# Generated by Django 2.1.2 on 2018-10-06 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country_info', '0003_auto_20181005_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['title']},
        ),
    ]
