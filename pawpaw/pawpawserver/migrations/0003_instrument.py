# Generated by Django 3.2 on 2021-04-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawpawserver', '0002_rename_pawpawserver_timeseriesdatum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
    ]
