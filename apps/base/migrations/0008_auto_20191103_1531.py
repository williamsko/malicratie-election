# Generated by Django 2.2.4 on 2019-11-03 15:31

from django.db import migrations, models
import utils.refs


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20191029_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundingtype',
            name='code',
            field=models.CharField(default=utils.refs.reference, max_length=255, unique=True),
        ),
    ]
