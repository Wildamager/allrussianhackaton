# Generated by Django 3.2.15 on 2022-12-11 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camerastream', '0002_alter_camers_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camers',
            old_name='locatin',
            new_name='location',
        ),
    ]
