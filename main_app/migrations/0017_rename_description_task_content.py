# Generated by Django 4.1.3 on 2022-11-30 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_task_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='content',
        ),
    ]
