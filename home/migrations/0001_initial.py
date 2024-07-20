# Generated by Django 4.1 on 2024-06-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('time', models.CharField(max_length=100)),
                ('speed', models.FloatField()),
                ('direction', models.FloatField()),
                ('height', models.FloatField()),
                ('did', models.CharField(max_length=100)),
                ('flag', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'home_coordinate',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Filename',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'home_filename',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coordinates', models.JSONField()),
                ('upload_count', models.PositiveIntegerField(default=1)),
                ('file_name', models.CharField(max_length=100)),
                ('time', models.JSONField()),
                ('speed', models.JSONField()),
                ('direction', models.JSONField()),
                ('height', models.JSONField()),
                ('did', models.JSONField()),
                ('flag', models.JSONField()),
                ('start_coor', models.JSONField()),
            ],
        ),
    ]