# Generated by Django 4.2.6 on 2023-10-25 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_habit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='last_reminder_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата последнего напоминания'),
        ),
    ]