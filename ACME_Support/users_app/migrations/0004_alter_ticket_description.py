# Generated by Django 4.1.6 on 2023-02-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_userprofile_alter_ticket_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]