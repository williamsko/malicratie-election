# Generated by Django 2.2.4 on 2019-11-18 10:09

from django.db import migrations, models
import django.db.models.deletion
import publication.models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0015_auto_20191118_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='content_img',
            field=models.FileField(blank=True, null=True, upload_to=publication.models.Publication.publication_directory_path),
        ),
        migrations.AlterField(
            model_name='publication',
            name='content_video',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Contenu video'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='quizz',
            field=models.ForeignKey(blank=True, help_text='Quizz', max_length=128, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='publication.Quizz'),
        ),
    ]
