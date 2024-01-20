# Generated by Django 4.2.6 on 2023-12-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_tbl_event_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_event',
            old_name='food',
            new_name='time',
        ),
        migrations.AddField(
            model_name='tbl_event',
            name='people_count',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_event',
            name='plan_name',
            field=models.CharField(default=5, max_length=30),
            preserve_default=False,
        ),
    ]
