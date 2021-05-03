# Generated by Django 2.2.4 on 2019-11-12 23:06

from django.db import migrations, models
import utils.refs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default=utils.refs.reference, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('status', models.BooleanField(default=True, help_text='Staut opérateur', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Operateur',
                'verbose_name_plural': 'Operateurs',
            },
        ),
        migrations.CreateModel(
            name='Parametrage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_adress', models.CharField(max_length=255, null=True, verbose_name='Adresse IP')),
                ('operateur', models.CharField(max_length=255, null=True, verbose_name='Opérateur')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Paramétrage',
                'verbose_name_plural': 'Paramétrages',
            },
        ),
        migrations.CreateModel(
            name='SmsReceived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, null=True, verbose_name='Numero')),
                ('sms_content', models.CharField(max_length=255, verbose_name='Contenu SMS')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Sms Received',
                'verbose_name_plural': 'Sms Received',
            },
        ),
        migrations.CreateModel(
            name='SmsResponseParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Code')),
                ('meaning', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Sms Response Parameter',
                'verbose_name_plural': 'Sms Response Parameter',
            },
        ),
        migrations.CreateModel(
            name='UssdRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Code')),
                ('meaning', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Sms Response Parameter',
                'verbose_name_plural': 'Sms Response Parameter',
            },
        ),
        migrations.CreateModel(
            name='UssdResponseParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Code')),
                ('response', models.CharField(max_length=255, verbose_name='Response')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Ussd Response Parameter',
                'verbose_name_plural': 'Ussd Response Parameter',
            },
        ),
    ]
