# Generated by Django 5.0.4 on 2024-05-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_rename_commentold_agreement_admincomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='IsUserAswerCommnet',
            field=models.BooleanField(null=True, verbose_name='Ответил ли пользователь на согласование'),
        ),
    ]
