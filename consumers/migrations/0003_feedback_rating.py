# Generated by Django 5.1.1 on 2024-10-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0002_feedback_replied_at_feedback_reply_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
