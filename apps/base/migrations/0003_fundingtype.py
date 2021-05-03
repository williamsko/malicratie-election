# Generated by Django 2.2.4 on 2019-10-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_projecttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('status', models.BooleanField(default=True, help_text="Funding's type  status in the system", verbose_name='Status')),
            ],
            options={
                'verbose_name': "Funding's type",
                'verbose_name_plural': "Funding' type",
            },
        ),
    ]
