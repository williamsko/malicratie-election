# Generated by Django 2.2.4 on 2020-01-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0010_auto_20191118_1106'),
        ('users', '0003_auto_20200108_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='geo_zone',
        ),
        migrations.AddField(
            model_name='profile',
            name='geo_zone',
            field=models.ManyToManyField(blank=True, max_length=128, null=True, to='geo.Geo'),
        ),
    ]