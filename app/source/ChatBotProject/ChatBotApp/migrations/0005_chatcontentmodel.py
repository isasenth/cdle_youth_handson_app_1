# Generated by Django 4.1.1 on 2023-03-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBotApp', '0004_remove_chatbotmodel_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
