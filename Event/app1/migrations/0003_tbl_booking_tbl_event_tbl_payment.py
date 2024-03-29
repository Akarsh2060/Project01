# Generated by Django 4.2.7 on 2023-12-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_name_tbl_register_uname'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=50)),
                ('event_name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('hotel_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('food', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tbl_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.IntegerField()),
                ('event_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
