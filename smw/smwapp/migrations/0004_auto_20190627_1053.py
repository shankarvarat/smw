# Generated by Django 2.1 on 2019-06-27 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smwapp', '0003_auto_20190627_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frends',
            old_name='frend',
            new_name='profile',
        ),
    ]
