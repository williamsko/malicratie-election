# Generated by Django 2.2.4 on 2019-11-08 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20191103_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'Description AJCAD', 'verbose_name_plural': 'Description AJCAD'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Catégorie de publication', 'verbose_name_plural': 'Catégories de publication'},
        ),
        migrations.AlterModelOptions(
            name='fundingtype',
            options={'verbose_name': "Type d'investissement", 'verbose_name_plural': "Types d'investissements"},
        ),
        migrations.AlterModelOptions(
            name='geo',
            options={'verbose_name': 'Découpage ', 'verbose_name_plural': 'Découpages '},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Partenaire Ajcad', 'verbose_name_plural': 'Partenaires Ajcad'},
        ),
        migrations.AlterModelOptions(
            name='projecttype',
            options={'verbose_name': 'Type de projet', 'verbose_name_plural': 'Types de projets'},
        ),
    ]
