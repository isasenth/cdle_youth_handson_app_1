# Generated by Django 4.1.1 on 2023-03-27 09:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBotApp', '0006_rename_name_chatcontentmodel_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatcontentmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
