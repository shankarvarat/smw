# Generated by Django 2.1 on 2019-05-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('Aid', models.IntegerField(auto_created=True, max_length=4, primary_key=True, serialize=False)),
                ('Aname', models.CharField(max_length=80)),
                ('Adob', models.DateField()),
            ],
        ),
    ]