# Generated by Django 3.1.1 on 2021-03-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210306_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdsurlimport',
            name='is_downloaded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sdsurlimport',
            name='is_duplicate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sdsurlimport',
            name='is_sds',
            field=models.BooleanField(default=False),
        ),
    ]