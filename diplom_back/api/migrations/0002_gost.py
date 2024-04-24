# Generated by Django 5.0.4 on 2024-04-22 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GOST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gostName', models.CharField(db_column='GostName', default='No name', max_length=128)),
                ('creationDate', models.DateField(auto_now_add=True)),
                ('lastModified', models.DateField(auto_now=True)),
                ('file', models.FileField(upload_to='GOST')),
                ('idCreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]