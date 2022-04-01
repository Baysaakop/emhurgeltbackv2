# Generated by Django 3.1.4 on 2022-03-24 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220323_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='bonus',
            new_name='bonus_used',
        ),
        migrations.AddField(
            model_name='customuser',
            name='bonus_collected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='bonus_granted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bonus',
            field=models.IntegerField(default=1000),
        ),
    ]