# Generated by Django 3.2 on 2021-05-05 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_rename_messages_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Chat Message', 'verbose_name_plural': 'Chat Messages'},
        ),
    ]
