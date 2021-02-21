# Generated by Django 3.1.5 on 2021-02-13 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='stage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='todo',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('next', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.comment')),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.comment'),
        ),
    ]
