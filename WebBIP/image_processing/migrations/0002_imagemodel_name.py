# Generated by Django 4.2.11 on 2024-03-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
