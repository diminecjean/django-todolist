# Generated by Django 4.2.4 on 2023-08-11 03:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_rename_title_todo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
