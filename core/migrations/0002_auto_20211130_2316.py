# Generated by Django 2.2 on 2021-11-30 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='bilen', max_length=255),
            preserve_default=False,
        ),
    ]
