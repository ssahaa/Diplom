# Generated by Django 5.0.4 on 2024-05-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_agreement_newname'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='IsNewTP',
            field=models.BooleanField(default=False, verbose_name='Явлется ли новым ТП'),
        ),
    ]