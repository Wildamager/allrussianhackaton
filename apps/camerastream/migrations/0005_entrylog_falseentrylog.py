# Generated by Django 3.2.15 on 2022-12-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camerastream', '0004_auto_20221211_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=126)),
                ('name', models.CharField(max_length=126)),
                ('date', models.CharField(max_length=126)),
            ],
        ),
        migrations.CreateModel(
            name='FalseEntryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=126)),
                ('image', models.ImageField(upload_to='false_entry')),
                ('date', models.CharField(max_length=126)),
            ],
        ),
    ]
