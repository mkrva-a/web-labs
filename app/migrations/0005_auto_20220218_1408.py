# Generated by Django 2.2.27 on 2022-02-18 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220218_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 2, 18, 14, 8, 58, 544741), verbose_name='Опубликована'),
        ),
    ]
