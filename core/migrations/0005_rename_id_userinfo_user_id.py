# Generated by Django 4.0.3 on 2024-03-10 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_userinfo_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='id',
            new_name='user_id',
        ),
    ]