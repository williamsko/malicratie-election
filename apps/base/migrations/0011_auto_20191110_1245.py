# Generated by Django 2.2.4 on 2019-11-10 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20191110_1245'),
        ('publication', '0013_remove_publication_category'),
        ('base', '0010_delete_geo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='FundingType',
        ),
        migrations.DeleteModel(
            name='ProjectType',
        ),
    ]
