# Generated by Django 3.1.4 on 2022-03-21 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220319_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='percent',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(default=users.models.create_new_ref_number, max_length=10, unique=True)),
                ('total', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField(blank=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_payed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(blank=True, null=True, to='users.CartItem')),
            ],
        ),
    ]
