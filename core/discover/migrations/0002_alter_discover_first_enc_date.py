# Generated by Django 4.1.3 on 2022-11-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discover',
            name='first_enc_date',
            field=models.DateField(),
        ),
    ]
