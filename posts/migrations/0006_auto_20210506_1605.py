# Generated by Django 3.2 on 2021-05-06 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_merge_0002_remove_post_title_0004_auto_20210505_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='created_at',
        ),
    ]