# Generated by Django 4.0.2 on 2022-03-30 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priority',
            old_name='status_id',
            new_name='status',
        ),
        migrations.AlterModelTable(
            name='priority',
            table='priority',
        ),
    ]