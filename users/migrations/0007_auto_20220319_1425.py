# Generated by Django 3.1.4 on 2022-03-19 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20220319_1425'),
        ('users', '0006_auto_20220318_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite',
            field=models.ManyToManyField(blank=True, null=True, to='items.Item'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='percent',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, to='users.CartItem'),
        ),
    ]