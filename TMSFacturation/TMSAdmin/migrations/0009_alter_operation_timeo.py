# Generated by Django 4.0.4 on 2022-06-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMSAdmin', '0008_alter_operation_distanceo_alter_operation_timeo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='timeO',
            field=models.CharField(max_length=6),
        ),
    ]
