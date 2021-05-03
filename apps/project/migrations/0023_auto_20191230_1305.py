# Generated by Django 2.2.4 on 2019-12-30 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_auto_20191226_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='investment_type',
            field=models.ForeignKey(blank=True, max_length=128, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.FundingType'),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(blank=True, max_length=128, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.ProjectType'),
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.BigIntegerField(blank=True, max_length=20, null=True),
        ),
    ]
