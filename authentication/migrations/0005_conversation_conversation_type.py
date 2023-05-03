# Generated by Django 4.2 on 2023-04-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_remove_conversation_conversation_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversation",
            name="conversation_type",
            field=models.CharField(
                choices=[("chat", "Chat"), ("pdf", "PDF")],
                default="chat",
                max_length=50,
            ),
        ),
    ]
