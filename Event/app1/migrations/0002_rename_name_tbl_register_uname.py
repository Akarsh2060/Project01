# Generated by Django 4.2.6 on 2023-11-24 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_register',
            old_name='name',
            new_name='uname',
        ),
    ]
