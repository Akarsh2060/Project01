# Generated by Django 4.0.4 on 2023-12-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_tbl_event_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_category',
            name='food',
            field=models.IntegerField(),
        ),
    ]
