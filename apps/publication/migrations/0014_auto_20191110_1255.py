# Generated by Django 2.2.4 on 2019-11-10 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0013_remove_publication_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('status', models.BooleanField(default=True, help_text="Category's status in the system", verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Catégorie de publication',
                'verbose_name_plural': 'Catégories de publication',
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(help_text='Categorie', max_length=128, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='publication.Category'),
        ),
    ]