# Generated by Django 5.0.4 on 2024-04-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_agreement_idactual'),
    ]

    operations = [
        migrations.AddField(
            model_name='tp',
            name='password',
            field=models.CharField(db_column='password', default='pass123', max_length=128, verbose_name='Пароль'),
        ),
    ]
