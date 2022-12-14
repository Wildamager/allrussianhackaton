# Generated by Django 3.2.15 on 2022-12-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20221210_0646'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Last_Name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Middle_Name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='left_photo',
        ),
        migrations.RemoveField(
            model_name='person',
            name='right_photo',
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=1, upload_to='persones'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='contact',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default=1, upload_to='persones'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='person',
            table='employee',
        ),
    ]
