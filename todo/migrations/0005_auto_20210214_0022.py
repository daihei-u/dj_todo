# Generated by Django 3.1.5 on 2021-02-14 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210214_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='confident',
            field=models.IntegerField(default='2'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='confidentioal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.confidentioal'),
        ),
    ]
