# Generated by Django 4.2.4 on 2023-08-10 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todo_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='name',
        ),
    ]
