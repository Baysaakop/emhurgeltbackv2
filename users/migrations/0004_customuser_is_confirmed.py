# Generated by Django 3.1.4 on 2022-03-18 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220318_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]