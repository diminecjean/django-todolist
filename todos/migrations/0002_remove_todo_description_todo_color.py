# Generated by Django 4.2.4 on 2023-08-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.AddField(
            model_name='todo',
            name='color',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
