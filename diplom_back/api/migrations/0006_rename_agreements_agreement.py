# Generated by Django 5.0.4 on 2024-04-24 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_agreements_comment_alter_agreements_commentold_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agreements',
            new_name='Agreement',
        ),
    ]
