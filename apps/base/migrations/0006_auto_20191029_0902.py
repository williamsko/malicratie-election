# Generated by Django 2.2.4 on 2019-10-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geo',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
