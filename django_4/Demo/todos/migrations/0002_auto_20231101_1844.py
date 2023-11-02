# Generated by Django 3.2.12 on 2023-11-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]