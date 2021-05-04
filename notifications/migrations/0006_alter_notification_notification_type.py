# Generated by Django 3.2 on 2021-05-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_notification_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('N', 'Notify'), ('NE', 'Notify With Email')], max_length=100),
        ),
    ]
