# Generated by Django 4.1.1 on 2022-12-27 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBotApp', '0003_users_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatbotmodel',
            name='created_at',
        ),
    ]
