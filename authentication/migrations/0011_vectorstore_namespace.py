# Generated by Django 4.2 on 2023-05-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0010_alter_pdfdocument_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="vectorstore",
            name="namespace",
            field=models.CharField(default="", max_length=255),
        ),
    ]
